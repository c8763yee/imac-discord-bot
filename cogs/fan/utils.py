import datetime
import json
import os
import re
from enum import IntEnum
from typing import Optional


import discord
from aiomqtt import Client
from dotenv import load_dotenv

from cogs import CogsExtension
from core.models import Field

from loggers import setup_package_logger

if os.path.exists('.env'):
    load_dotenv('.env', verbose=True, override=True)

MQTT_BROKER: str = os.getenv('MQTT_BROKER', 'localhost')
MQTT_PORT: int = int(os.getenv('MQTT_PORT', 1883))


logger = setup_package_logger(__name__)


class FanPosition(IntEnum):
    BACK_DOOR = 1
    FRONT_DOOR = 2
    MEETING_ROOM = 3


TURN_ON_FAN_PAYLOAD = {
    FanPosition.BACK_DOOR: {
        'fan_0': 'OUT',
        'fan_1': 'OUT'
    },
    FanPosition.FRONT_DOOR: {
        'fan_0': 'IN',
        'fan_1': 'IN'
    },
    FanPosition.MEETING_ROOM: {'fan_0': 'IN'}
}

TURN_OFF_FAN_PAYLOAD = {
    FanPosition.BACK_DOOR: {
        'fan_0': 'OFF',
        'fan_1': 'OFF'
    },
    FanPosition.FRONT_DOOR: {
        'fan_0': 'OFF',
        'fan_1': 'OFF'
    },
    FanPosition.MEETING_ROOM: {'fan_0': 'OFF'}
}

class FanUtils(CogsExtension):
    TOPIC_PREFIX = "2706/IAQ"
    
    async def turn_on(self, fan_position: FanPosition) -> str:
        async with Client(MQTT_BROKER, MQTT_PORT) as client:
            await client.publish(f"{self.TOPIC_PREFIX}/{fan_position}/control",
                                 json.dumps(TURN_ON_FAN_PAYLOAD[fan_position]))
        return f"Turned on fan {fan_position.name}"

    async def turn_off(self, fan_position: FanPosition) -> str:
        async with Client(MQTT_BROKER, MQTT_PORT) as client:
            await client.publish(f"{self.TOPIC_PREFIX}/{fan_position}/control",
                                 json.dumps(TURN_OFF_FAN_PAYLOAD[fan_position]))
            
        return f"Turned off fan {fan_position.name}"

