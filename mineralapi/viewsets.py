from rest_framework import viewsets
from . import models
from . import serializers

class MineralViewset(viewsets.ModelViewSet):
    queryset = models.Mineral.objects.all()
    serializer_class = serializers.MineralSerializer

class StatusViewset(viewsets.ModelViewSet):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer