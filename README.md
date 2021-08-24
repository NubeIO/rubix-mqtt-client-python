# rubix-mqtt-client

___
### Example

```bash
cp config.example.json config.json

python example.py
```

---

### MQTT responses

##### <kbd>method</kbd> `rubix.rubix_mqtt.get_mqtt_responses()`
Get mqtt responses

```bash
return {
  <device_id>:{
    "client_id": <client_id>,
    "site_id": <site_id>,
    "device_id": <device_id>,
    "points":[
      {
        "uuid":<uuid>,
        "name":<uuid>
      },
      ...
    ],
    "schedules":[
      {
        "uuid":<uuid>,
        "name":<name>
      },
      ...
    ]
  },
  ...
}
```

---

### Points

#### <kbd>method</kbd> `rubix.rubix_point.get_points()`
Get points
```bash
return {
  <device_id>:[
    {
      "uuid":<uuid>,
      "name":<name>
    },
    ...
  ],
  <device_id>:[
    {
      "uuid":<uuid>,
      "name":<name>
    },
    ...
  ],
  ...
}
```

#### <kbd>method</kbd> `rubix.rubix_point.get_points_by_device_id(device_id)`
Get points by device_id
```bash
return [
    {
      "uuid":<uuid>,
      "name":<name>
    },
    ...
]
```

---
### Point value

#### <kbd>method</kbd> `rubix.rubix_point.write_point_value(device_id, uuid, priority, value)`
Write point value

---
### Schedules

#### <kbd>method</kbd> `rubix.rubix_schedule.get_schedule()`
Get schedules
```bash
return {
  <device_id>:[
    {
      "uuid":<uuid>,
      "name":<name>
    },
    ...
  ],
  <device_id>:[
    {
      "uuid":<uuid>,
      "name":<name>
    },
    ...
  ],
  ...
}
```

#### <kbd>method</kbd> `rubix.rubix_schedule.get_schedules(device_id)`
Get schedules by device_id
```bash
return [
    {
      "uuid":<uuid>,
      "name":<name>
    },
    ...
]
```

---
### Schedule value

#### <kbd>method</kbd> `rubix.rubix_schedule.write_schedule_value_by_uuid(device_id, uuid, payload)`
Write schedule value by uuid

#### <kbd>method</kbd> `rubix.rubix_schedule.write_schedule_value_by_name(device_id, name, payload)`
Write schedule value by name

```bash
payload = {
    "events": {
        "QhovV9c2xh4xh5SDT3NBQ5": {
            "name": "TRAINING EVENT",
            "dates": [
                {
                    "start": "2021-08-23T23:15:00.000Z",
                    "end": "2021-08-24T00:15:00.000Z"
                }
            ],
            "value": 20,
            "color": ""
        }
    },
    "weekly": {
        "cjuVMsaXUvgpYYsmVA5tv7": {
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
            "value": 11,
            "color": "#d0021b"
        }
    },
    "holiday": {
        "UFckPkfDGVzUzsa7Qhebsb": {
            "id": "UFckPkfDGVzUzsa7Qhebsb",
            "name": "HOLIDAY TEST",
            "color": {
                "dispatchConfig": null,
                "_targetInst": null,
                "nativeEvent": null,
                "type": null,
                "target": null,
                "currentTarget": null,
                "eventPhase": null,
                "bubbles": null,
                "cancelable": null,
                "timeStamp": null,
                "defaultPrevented": null,
                "isTrusted": null,
                "_dispatchListeners": null,
                "_dispatchInstances": null
            },
            "date": "08-24",
            "value": 15
        }
    }
}
```
---


