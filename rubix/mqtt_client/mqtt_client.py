import time

from rubix_mqtt.mqtt import MqttClientBase

from rubix.store import update_store
from rubix.utils.singleton import Singleton


class MqttClient(MqttClientBase, metaclass=Singleton):

    def __init__(self):
        super().__init__()

    def _on_message(self, client, userdata, message):
        update_store(message)

    def publish_value(self, topic: str, payload: str, retain: bool = True):
        if not self.config:
            return
        timeout: int = self.config.timeout
        start_time: float = time.time()
        while True:
            if self.status():
                self.client.publish(topic, payload, qos=self.config.qos, retain=retain)
                return
            else:
                if time.time() - start_time <= timeout:
                    time.sleep(0.01)
                else:
                    print(f'Failed to publish value: {payload}, on topic: {topic}')
                    return
