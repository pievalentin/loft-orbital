from django.db import models


# Create your models here.
class Temperature(models.Model):
    timestamp = models.DateTimeField()
    value = models.FloatField()

    def __str__(self):
        return f"Date: {self.timestamp.isoformat()}  Value:  {self.value}"
