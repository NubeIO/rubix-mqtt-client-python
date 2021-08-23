from typing import List

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
