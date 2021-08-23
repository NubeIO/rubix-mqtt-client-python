from random import randrange, uniform
from time import sleep

from rubix.mqtt_client.mqtt_listener import MqttListener
from rubix.rubix_mqtt import get_mqtt_responses
from rubix.rubix_point import get_points_by_device_id, update_point_value, get_points
from rubix.rubix_schedule import get_schedules_by_device_id, get_schedules
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
    Get Mqtt Responses
    """
    mqtt_responses = get_mqtt_responses()
    print('MQTT RESPONSES :', mqtt_responses)
    if mqtt_responses:
        device_id = list(mqtt_responses.keys())[0]
        """
        Get points
        """
        points = get_points()
        print('POINTS :', points)
        """
        Get device points
        """
        device_points = get_points_by_device_id(device_id)
        print('DEVICE POINTS :', device_points)
        if device_points:
            uuid: str = device_points[0].get('uuid')
            priority: int = randrange(1, 16)
            value: float = round(uniform(1.0, 16.0), 2)
            """
            Update point value
            """
            print(f'Update point value device_id:{device_id} uuid:{uuid}, priority:{priority}, value:{value})')
            update_point_value(device_id, uuid, priority, value)
        """
        Get schedules
        """
        schedules = get_schedules()
        print('SCHEDULES :', schedules)
        """
        Get schedules
        """
        device_schedules = get_schedules_by_device_id(device_id)
        print('DEVICE SCHEDULES :', device_schedules)
        break
    sleep(20)
