import json
from typing import List

from rubix.utils.singleton import Singleton


def update_store(message):
    topic = message.topic.split('/')
    client_id: str = topic[0]
    site_id: str = topic[2]
    device_id: str = topic[4]
    if topic[9] == 'points':
        points = json.loads(message.payload)
        if points:
            Store().append_points(client_id, site_id, device_id, points)
    elif topic[9] == 'schedules':
        schedules = json.loads(message.payload)
        if schedules:
            Store().append_schedules(client_id, site_id, device_id, schedules)


class Response:
    def __init__(self, client_id: str, site_id: str, device_id: str, points: List[dict],
                 schedules: List[dict]):
        self.client_id = client_id
        self.site_id = site_id
        self.device_id = device_id
        self.points = points or []
        self.schedules = schedules or []

    def __repr__(self):
        return json.dumps({
            'client_id': self.client_id,
            'site_id': self.site_id,
            'device_id': self.device_id,
            'points': self.points,
            'schedules': self.schedules
        })


class Store(metaclass=Singleton):
    def __init__(self):
        self.__responses: {[str]: Response} = {}

    def get(self):
        return self.__responses

    def get_by_device_id(self, device_id: str):
        return self.__responses.get(device_id)

    def append_points(self, client_id: str, site_id: str, device_id: str, points: List[dict]):
        if not self.__responses.get(device_id):
            self.__responses[device_id] = Response(client_id, site_id, device_id, points, [])
        else:
            self.__responses[device_id].client_id = client_id
            self.__responses[device_id].site_id = site_id
            self.__responses[device_id].device_id = device_id
            self.__responses[device_id].points = points

    def append_schedules(self, client_id: str, site_id: str, device_id: str, schedules: List[dict]):
        if not self.__responses.get(device_id):
            self.__responses[device_id] = Response(client_id, site_id, device_id, [], schedules)
        else:
            self.__responses[device_id].client_id = client_id
            self.__responses[device_id].site_id = site_id
            self.__responses[device_id].device_id = device_id
            self.__responses[device_id].schedules = schedules
