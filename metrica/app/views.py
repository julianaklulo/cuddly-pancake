from rest_framework import viewsets
from .serializers import TeamSerializer, PersonSerializer, MetricSerializer
from .models import Team, Person, Metric


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('name')
    serializer_class = PersonSerializer


class MetricViewSet(viewsets.ModelViewSet):
    queryset = Metric.objects.all().order_by('name')
    serializer_class = MetricSerializer
