import json
from typing import List

from rubix.mqtt_client.mqtt_client import MqttClient
from rubix.store import Store, Response


def get_schedules():
    schedules: dict = {}
    responses = Store().get()
    for key, value in responses.items():
        schedules = {**schedules, key: value.schedules}
    return schedules


def get_schedules_by_device_id(device_id: str) -> List:
    response: Response = Store().get_by_device_id(device_id)
    if response:
        return response.schedules
    return []


def write_schedule_value_by_uuid(device_id: str, uuid: str, payload: dict):
    device: Response = Store().get_by_device_id(device_id)
    if not device:
        return
    topic: str = f'{device.client_id}/{device.site_id}/{device.device_id}/rubix/points/listen/schedules/uuid/{uuid}'
    MqttClient().publish_value(topic, json.dumps(payload))


def write_schedule_value_by_name(device_id: str, name: str, payload: dict):
    device: Response = Store().get_by_device_id(device_id)
    if not device:
        return
    topic: str = f'{device.client_id}/{device.site_id}/{device.device_id}/rubix/points/listen/schedules/name/{name}'
    MqttClient().publish_value(topic, json.dumps(payload))
