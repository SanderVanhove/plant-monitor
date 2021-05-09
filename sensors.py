from dataclasses import dataclass

from seeed_dht import DHT
from grove.grove_light_sensor_v1_2 import GroveLightSensor
from grove.grove_moisture_sensor import GroveMoistureSensor


moisture_sensor = GroveMoistureSensor(6)
hum_temp_sensor = DHT('11', 16)
light_sensor = GroveLightSensor(0)


@dataclass
class SensorReading:
    light: float
    temperature: float
    humidity: float
    moisture: float


def get_metrics() -> SensorReading:
    """
    Read sensor metrics.
    """
    moisture = moisture_sensor.moisture
    humidity, temperature = hum_temp_sensor.read()
    light = light_sensor.light

    return SensorReading(light, temperature, humidity, moisture)
