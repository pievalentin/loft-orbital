from typing import Any
from django.test import TestCase
from graphene.test import Client
from graphene import Schema
from loft_orbital.temp_monitoring.schema import Query, TemperatureStatisticsType
# Make sure we can retrieve the latest temperature from graphene


class TestLatestTemperature(TestCase):
    fixtures: Any = ['temps.json']
    schema: Schema = Schema(query=Query)

    def test_temperature_stat_query(self):
        client = Client(self.schema)
        executed = client.execute('''{
        temperatureStatistics(after:"2022-06-23T19:40:52.809933+00:00", before:"2022-06-23T20:39:52.740649+00:00"){
        min,
        max
    }
    }''')
        assert executed == {
            "data": {
                "temperatureStatistics": {
                    "min": -0.86033105288625,
                    "max": -26.322787257083206
                }
            }
        }

    def test_out_of_range_query(self):
        client = Client(self.schema)
        executed = client.execute('''{
        temperatureStatistics(after:"2022-06-23T22:40:52.809933+00:00", before:"2022-06-23T20:39:52.740649+00:00"){
        min,
        max
    }
    }''')
        assert executed == {
            "data": {
                "temperatureStatistics": None
            }
        }

    def test_current_temperature_query(self):
        client = Client(self.schema)
        executed = client.execute('''{
        currentTemperature{
        timestamp,
        value
    }
    }''')
        assert executed == {
            "data": {
                "currentTemperature": {
                    "timestamp": "2022-06-23T19:41:22.833000+00:00",
                    "value": -0.86033105288625
                }
            }
        }
