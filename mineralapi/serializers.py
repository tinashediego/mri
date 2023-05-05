
from rest_framework import serializers
from .models import Mineral, Status

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class MineralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mineral
        fields = '__all__'
        depth = 2


        

