import json
import os

from aiomqtt import Client
from dotenv import load_dotenv
from loggers import setup_package_logger

from cogs import CogsExtension

if os.path.exists(".env"):
    load_dotenv(".env", verbose=True, override=True)

MQTT_BROKER: str = os.getenv("MQTT_BROKER", "localhost")
MQTT_PORT: int = int(os.environ.get("MQTT_PORT", 1883))


logger = setup_package_logger(__name__)


TURN_ON_AIRCONDITION_PAYLOAD = {"Status": "On"}

TURN_OFF_AIRCONDITION_PAYLOAD = {"Status": "Off"}


class AirConditionUtils(CogsExtension):
    TOPIC = "2706/Air_Condiction/A"

    async def turn_on(self, temperature: int = 25) -> str:
        async with Client(MQTT_BROKER, MQTT_PORT) as client:
            TURN_ON_AIRCONDITION_PAYLOAD["Temp"] = str(temperature)
            await client.publish(
                f"{self.TOPIC}/control", json.dumps(TURN_ON_AIRCONDITION_PAYLOAD)
            )
        return f"Turned on aircondition with temperature {temperature}"

    async def turn_off(self) -> str:
        async with Client(MQTT_BROKER, MQTT_PORT) as client:
            await client.publish(
                f"{self.TOPIC}/control", json.dumps(TURN_OFF_AIRCONDITION_PAYLOAD)
            )

        return "Turned off aircondition"

    async def get_stat(self) -> dict:
        async with Client(MQTT_BROKER, MQTT_PORT) as client:
            await client.subscribe(self.TOPIC)
            async for message in client.messages:
                return json.loads(message.payload)
