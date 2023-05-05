from django.contrib import admin

# Register your models here.
from .models import OreOutput, GrossRevenue, NetProfit, TaxesPaid, Source, Mine,CoperateSocialResponsibility,Company

admin.site.register(OreOutput)
admin.site.register(GrossRevenue)
admin.site.register(NetProfit)
admin.site.register(TaxesPaid)
admin.site.register(Source)
admin.site.register(Mine)
admin.site.register(CoperateSocialResponsibility)
admin.site.register(Company)

