# rubix-mqtt-client

___

### Config

#### Example

```bash
cp config.example.json config/config.json

python example.py
```

---

#### MQTT responses

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

#### Points

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
#### Point value

#### <kbd>method</kbd> `rubix.rubix_point.update_point_value(device_id, uuid, priority, value)`
Update point value

---
#### Schedules

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


