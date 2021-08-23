import json

from rubix.mqtt_client.mqtt_client import MqttClient
from rubix.store import StorePoints


def get_points():
    return StorePoints().points()


def get_point_topic():
    return StorePoints().topic()


def update_point_value(uuid: str, priority: int = 16, value: float = 0):
    topic: str = f'{StorePoints().topic()}{uuid}'
    payload: str = json.dumps({'value': value, 'priority': priority})
    MqttClient().publish_value(topic, payload)
