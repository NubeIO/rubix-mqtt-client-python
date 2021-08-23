import json
import os

from rubix_mqtt.setting import MqttSettingBase


class MqttSetting(MqttSettingBase):
    KEY = 'mqtt_client'

    def __init__(self):
        super().__init__()
        self.enabled = False
        self.master = False
        self.name = 'mqtt_client'
        self.client_id = ''


class AppSetting:
    fallback_logging_conf: str = 'config/logging.conf'

    def __init__(self):
        self.__mqtt_setting: MqttSetting = MqttSetting()

    def load(self, **kwargs):
        config_dir: str = kwargs.get('file') or os.getcwd()
        file = f"{config_dir}/config.json"
        data = self.__read_file(file)
        self.__mqtt_setting = self.__mqtt_setting.reload(data.get('mqtt'))
        return self

    def mqtt_setting(self):
        return self.__mqtt_setting

    def reload(self, setting: dict):
        if setting is not None:
            self.__dict__ = {k: setting.get(k, v) for k, v in self.__dict__.items()}
        return self

    @staticmethod
    def __read_file(file_path: str):
        if not os.path.isfile(file_path) or not os.path.exists(file_path):
            return {}
        with open(file_path) as json_file:
            return json.load(json_file)
