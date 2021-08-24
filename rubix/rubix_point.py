import json
from typing import List

from rubix.mqtt_client.mqtt_client import MqttClient
from rubix.store import Store, Response


def get_points() -> dict:
    points: dict = {}
    responses = Store().get()
    for key, value in responses.items():
        points = {**points, key: value.points}
    return points


def get_points_by_device_id(device_id: str) -> List:
    response: Response = Store().get_by_device_id(device_id)
    if response:
        return response.points
    return []


def write_point_value(device_id: str, uuid: str, priority: int, value: float):
    device: Response = Store().get_by_device_id(device_id)
    if not device:
        return
    topic: str = f'{device.client_id}/{device.site_id}/{device.device_id}/rubix/points/listen/cov/uuid/{uuid}'
    payload: str = json.dumps({'value': value, 'priority': priority})
    MqttClient().publish_value(topic, payload)
