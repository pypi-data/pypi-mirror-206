import asyncio
import json
from asyncio import Task
from typing import Any
from typing import Optional
from typing import Set
from typing import Tuple

from asyncio_mqtt import Client

from unipi_control.config import Config
from unipi_control.config import DEVICE_CLASSES
from unipi_control.config import HardwareData
from unipi_control.config import logger
from unipi_control.integrations.covers import CoverMap
from unipi_control.log import LOG_MQTT_PUBLISH


class HassCoversDiscovery:
    """Provide the covers as Home Assistant MQTT discovery."""

    def __init__(self, covers: CoverMap, neuron, mqtt_client: Client) -> None:
        self.mqtt_client: Client = mqtt_client
        self.covers: CoverMap = covers

        self.config: Config = neuron.config
        self.hardware: HardwareData = neuron.hardware

    def _get_discovery(self, cover) -> Tuple[str, dict]:
        topic: str = f"{self.config.homeassistant.discovery_prefix}/cover/{cover.unique_id}/config"
        device_name: str = self.config.device_info.name
        via_device: Optional[str] = None

        if cover.suggested_area:
            via_device = device_name
            device_name = f"{device_name} - {cover.suggested_area}"

        message: dict = {
            "name": cover.friendly_name,
            "unique_id": f"{cover.unique_id}",
            "command_topic": f"{cover.topic}/set",
            "state_topic": f"{cover.topic}/state",
            "qos": 2,
            "optimistic": False,
            "device": {
                "name": device_name,
                "identifiers": device_name,
                "model": f'{self.hardware["neuron"].name} {self.hardware["neuron"].model}',
                "manufacturer": self.config.device_info.manufacturer,
            },
        }

        if cover.object_id:
            message["object_id"] = cover.object_id

        if cover.suggested_area:
            message["device"]["suggested_area"] = cover.suggested_area

        if via_device:
            message["device"]["via_device"] = via_device

        if cover.settings.set_position:
            message["position_topic"] = f"{cover.topic}/position"
            message["set_position_topic"] = f"{cover.topic}/position/set"

        if cover.settings.set_tilt:
            message["tilt_status_topic"] = f"{cover.topic}/tilt"
            message["tilt_command_topic"] = f"{cover.topic}/tilt/set"

        return topic, message

    async def publish(self) -> None:
        """Publish MQTT Home Assistant discovery topics for covers."""
        for cover in self.covers.by_device_classes(DEVICE_CLASSES):
            topic, message = self._get_discovery(cover)
            json_data: str = json.dumps(message)
            await self.mqtt_client.publish(topic, json_data, qos=2, retain=True)
            logger.debug(LOG_MQTT_PUBLISH, topic, json_data)


class HassCoversMqttPlugin:
    """Provide Home Assistant MQTT commands for covers."""

    def __init__(self, neuron, mqtt_client, covers: CoverMap) -> None:
        self._hass = HassCoversDiscovery(covers, neuron, mqtt_client)

    async def init_tasks(self, tasks: Set[Task]) -> None:
        """Initialize MQTT tasks for publish MQTT topics.

        Parameters
        ----------
        tasks: set
            A set of all MQTT tasks.
        """
        task: Task[Any] = asyncio.create_task(self._hass.publish())
        tasks.add(task)
