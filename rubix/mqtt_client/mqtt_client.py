import logging
import time

from rubix_mqtt.mqtt import MqttClientBase

from rubix.store import update_store
from rubix.utils.singleton import Singleton

logger = logging.getLogger(__name__)


class MqttClient(MqttClientBase, metaclass=Singleton):

    def __init__(self):
        super().__init__()

    def _on_message(self, client, userdata, message):
        update_store(message)

    def publish_value(self, topic: str, payload: str):
        if not self.config:
            return
        timeout: int = self.config.timeout
        start_time: float = time.time()
        while True:
            if self.status():
                self.client.publish(topic, payload, self.config.qos)
                return
            else:
                if time.time() - start_time <= timeout:
                    time.sleep(0.01)
                else:
                    print(f'Failed to publish value: {payload}, on topic: {topic}')
                    logger.error(f'Failed to publish value: {payload}, on topic: {topic}')
                    return
