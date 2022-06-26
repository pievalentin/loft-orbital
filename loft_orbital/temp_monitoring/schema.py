import graphene
from graphene_django import DjangoObjectType

from loft_orbital.temp_monitoring.models import Temperature


class TemperatureType(DjangoObjectType):
    class Meta:
        model = Temperature
        fields = ("timestamp", "value")


class TemperatureStatisticsType(graphene.ObjectType):
    min = graphene.Float()
    max = graphene.Float()


class Query(graphene.ObjectType):
    current_temperature = graphene.Field(TemperatureType)
    temperature_statistics = graphene.Field(
        TemperatureStatisticsType, after=graphene.DateTime(), before=graphene.DateTime()
    )

    def resolve_current_temperature(root, info):
        return Temperature.objects.latest("timestamp")

    def resolve_temperature_statistics(root, info, after, before):
        window = Temperature.objects.filter(
            timestamp__gte=after, timestamp__lte=before
        ).order_by("-value")
        if not window:
            return None
        else:
            return {"min": window.first().value, "max": window.last().value}


schema = graphene.Schema(query=Query)
