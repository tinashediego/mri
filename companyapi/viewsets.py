from rest_framework import viewsets
from . import models
from . import serializers

class CompanyViewset(viewsets.ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer

class GrossRevenueViewset(viewsets.ModelViewSet):
    queryset = models.GrossRevenue.objects.all()
    serializer_class = serializers.GrossRevenueSerializer

class NetProfitViewset(viewsets.ModelViewSet):
    queryset = models.NetProfit.objects.all()
    serializer_class = serializers.NetProfitSerializer

class TaxesPaidViewset(viewsets.ModelViewSet):
    queryset = models.TaxesPaid.objects.all()
    serializer_class = serializers.TaxesPaidSerializer

class SourceViewset(viewsets.ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer

class MineViewset(viewsets.ModelViewSet):
    queryset = models.Mine.objects.all()
    serializer_class = serializers.MineSerializer

class CoperateSocialResponsibilityViewset(viewsets.ModelViewSet):
    queryset = models.CoperateSocialResponsibility.objects.all()
    serializer_class = serializers.CoperateSocialResponsibilitySerializer

class SourceViewset(viewsets.ModelViewSet):
    queryset = models.Source.objects.all()
    serializer_class = serializers.SourceSerializer