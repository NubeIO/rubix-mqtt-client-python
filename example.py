from random import randrange, uniform
from time import sleep

from rubix import rubix_point
from rubix.mqtt_client.mqtt_listener import MqttListener
from rubix.setting import AppSetting

"""
App Setting
"""
app_setting = AppSetting()
app_setting.load()

"""
MQTT Listener
"""
MqttListener(mqtt_setting=app_setting.mqtt_setting()).start()

while True:
    """
    POINTS
    """
    points = rubix_point.get_points()
    if points:
        print('POINTS :', points)
        uuid: str = points[0].get('uuid')
        priority: int = randrange(1, 16)
        value: float = round(uniform(1.0, 16.0), 2)
        print(f'Update point value uuid:{uuid}, priority:{priority}, value:{value})')
        rubix_point.update_point_value(uuid, priority, value)
        sleep(60)
