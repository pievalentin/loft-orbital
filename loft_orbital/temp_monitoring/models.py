from django.db import models
from psycopg2 import Timestamp


# Create your models here.
class Temperature(models.Model):
    timestamp = models.DateTimeField()
    value = models.FloatField()

    def __str__(self):
        return f"Date: {self.timestamp.isoformat()}  Value:  {self.value}"
