import json
from typing import List

from rubix.utils.singleton import Singleton


def update_store(message):
    topic = message.topic.split('/')
    if topic[8] == 'value' and topic[9] == 'points':
        points = json.loads(message.payload)
        if points:
            point_topic: str = f'{topic[0]}/{topic[2]}/{topic[4]}/rubix/points/listen/cov/uuid/'
            StorePoints().update_topic(point_topic)
            StorePoints().update_points(points)


class StorePoints(metaclass=Singleton):
    def __init__(self):
        self.__points: List[dict] = []
        self.__topic: str = ''

    def points(self) -> List[dict]:
        return self.__points

    def topic(self) -> str:
        return self.__topic

    def update_points(self, points: List[dict]):
        self.__points = points

    def update_topic(self, topic: str):
        self.__topic = topic
