from typing import Callable, List

from rubix.setting import MqttSetting
from rubix.utils.singleton import Singleton


class MqttListener(metaclass=Singleton):
    def __init__(self, mqtt_setting: MqttSetting = MqttSetting(), callback: Callable = None):
        self.__mqtt_setting: MqttSetting = mqtt_setting
        self.__mqtt_setting.retain = False
        self.__callback: Callable = callback

    @property
    def mqtt_setting(self) -> MqttSetting:
        return self.__mqtt_setting

    def start(self):
        from rubix.mqtt_client.mqtt_client import MqttClient
        mqtt_client = MqttClient()
        subscribe_topics: List[str] = [f'{self.mqtt_setting.client_id}/+/+/+/+/+/rubix/points/value/points',
                                       f'{self.mqtt_setting.client_id}/+/+/+/+/+/rubix/points/value/schedules']
        mqtt_client.start(self.__mqtt_setting, subscribe_topics, self.__callback)

    @staticmethod
    def status():
        from rubix.mqtt_client.mqtt_client import MqttClient
        return MqttClient().status()
