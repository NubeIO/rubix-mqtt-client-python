from random import randrange, uniform
from time import sleep

import shortuuid

from rubix.mqtt_client.mqtt_listener import MqttListener
from rubix.rubix_mqtt import get_mqtt_responses
from rubix.rubix_point import get_points_by_device_id, write_point_value, get_points
from rubix.rubix_schedule import get_schedules_by_device_id, get_schedules, write_schedule_value_by_uuid, \
    write_schedule_value_by_name
from rubix.setting import AppSetting


def generate_schedule_value_payload() -> dict:
    events_key = shortuuid.uuid()
    weekly_key = shortuuid.uuid()
    holiday_key = shortuuid.uuid()
    return {
        "events": {
            events_key: {
                "name": "TRAINING EVENT",
                "dates": [
                    {
                        "start": "2021-08-23T23:15:00.000Z",
                        "end": "2021-08-24T00:15:00.000Z"
                    }
                ],
                "value": randrange(1, 20),
                "color": ""
            }
        },
        "weekly": {
            weekly_key: {
                "name": "WEEKLY TRAINING",
                "days": [
                    "sunday",
                    "monday",
                    "tuesday",
                    "wednesday",
                    "thursday"
                ],
                "start": "23:30",
                "end": "00:00",
                "value": randrange(1, 20),
                "color": "#d0021b"
            }
        },
        "holiday": {
            holiday_key: {
                "id": holiday_key,
                "name": "HOLIDAY TEST",
                "color": {
                    "dispatchConfig": None,
                    "_targetInst": None,
                    "nativeEvent": None,
                    "type": None,
                    "target": None,
                    "currentTarget": None,
                    "eventPhase": None,
                    "bubbles": None,
                    "cancelable": None,
                    "timeStamp": None,
                    "defaultPrevented": None,
                    "isTrusted": None,
                    "_dispatchListeners": None,
                    "_dispatchInstances": None
                },
                "date": "08-24",
                "value": randrange(1, 20)
            }
        }
    }


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
            Write point value
            """
            print(f'Write point value (device_id:{device_id}, uuid:{uuid}, priority:{priority}, value:{value}))')
            write_point_value(device_id, uuid, priority, value)
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
        if device_schedules:
            """
            Write schedule value by uuid
            """
            uuid: str = device_schedules[0].get('uuid')
            payload: dict = generate_schedule_value_payload()
            print(f'Write schedule value by uuid (device_id:{device_id}, uuid:{uuid}, payload:{payload})')
            write_schedule_value_by_uuid(device_id, uuid, payload)
            """
            Write schedule value by name
            """
            name: str = device_schedules[0].get('name')
            payload: dict = generate_schedule_value_payload()
            print(f'Write schedule value by name (device_id:{device_id}, uuid:{uuid}, payload:{payload})')
            write_schedule_value_by_name(device_id, name, payload)
        break
    sleep(20)
