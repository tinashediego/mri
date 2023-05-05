from django.db import models

from mineralapi.models import Mineral


# Create your models here.

class OreOutput(models.Model):
    id = models.AutoField(primary_key=True)
    name_of_the_mineral = models.ForeignKey(Mineral,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=False)
    year = models.CharField(max_length=10, blank=False)
    amount = models.BigIntegerField(blank=False)
    
    def __str__(self):
        return self.company_name+self.year

class GrossRevenue(models.Model):
    id = models.AutoField(primary_key=True)
    name_of_the_mineral = models.ForeignKey(Mineral,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=False)
    year = models.CharField(max_length=10, blank=False)
    amount = models.BigIntegerField(blank=False)
    
    def __str__(self):
        return self.company_name +self.year 

class NetProfit(models.Model):
    id = models.AutoField(primary_key=True)
    name_of_the_mineral = models.ForeignKey(Mineral,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=False)
    year = models.CharField(max_length=10, blank=False)
    amount = models.BigIntegerField(blank=False)
    
    def __str__(self):
        return self.company_name +self.year

class TaxesPaid(models.Model):
    id = models.AutoField(primary_key=True)
    name_of_the_mineral = models.ForeignKey(Mineral,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100, blank=False)
    year = models.CharField(max_length=10, blank=False)
    amount = models.BigIntegerField(blank=False)
    
    def __str__(self):
        return self.company_name+ self.year

class Source(models.Model):
    id = models.AutoField(primary_key=True)
    name_of_the_source = models.CharField(max_length=200,blank=False)
    url_link_to_the_source = models.CharField(max_length=200, blank=False)
    source_year = models.CharField(max_length=200,blank=False)
    
    def __str__(self):
        return self.name_of_the_source

class Mine(models.Model):
    id = models.AutoField(primary_key=True)
    name_of_the_mine = models.CharField(max_length=200,blank=False)
    location = models.CharField(max_length=200, blank=False)
    
    def __str__(self):
        return self.name_of_the_mine

class CoperateSocialResponsibility(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100, blank=False)
    year = models.CharField(max_length=10, blank=False)
    amount = models.BigIntegerField(blank=False)
    
    def __str__(self):
        return self.company_name + self.year

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100, blank=False)
    parent_company_name = models.CharField(max_length=100, blank=True)
    minerals_name = models.ManyToManyField(Mineral, blank=False)
    local_or_international = models.CharField(max_length=100, blank=True)
    head_office_country = models.CharField(max_length = 100, blank=True)
    number_of_mines = models.PositiveIntegerField(blank=False)
    list_of_mines = models.ManyToManyField(Mine, blank=True)
    average_percentage_of_CSR = models.FloatField(blank=True)
    ore_Output = models.ManyToManyField(OreOutput, blank=True)
    gross_revenue = models.ManyToManyField(GrossRevenue, blank=True)
    net_profit = models.ManyToManyField(NetProfit, blank=True)
    taxes_paid = models.ManyToManyField(TaxesPaid, blank=True)
    sources = models.ManyToManyField(Source, blank=True)
    average_percentage_of_CSR = models.ManyToManyField(CoperateSocialResponsibility, blank=True)

    def __str__(self):
        return self.company_name
