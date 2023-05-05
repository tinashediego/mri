
from rest_framework import serializers

from mineralapi.models import Mineral
from .models import Company, OreOutput, GrossRevenue, NetProfit, TaxesPaid, Source, Mine, CoperateSocialResponsibility

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        depth = 2

class OreOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = OreOutput
        fields = '__all__'
        
class GrossRevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrossRevenue
        fields = '__all__'

class NetProfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = NetProfit
        fields = '__all__'

class TaxesPaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxesPaid
        fields = '__all__'

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'

class MineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mine
        fields = '__all__'

class CoperateSocialResponsibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CoperateSocialResponsibility
        fields = '__all__'

class MineralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mineral
        fields = '__all__'
    