from django.db import models

# Create your models here.

class Status(models.Model):
    id = models.AutoField(primary_key=True)
    name_of_the_status = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name_of_the_status


class Mineral(models.Model):
    id = models.AutoField(primary_key=True)
    name_of_the_mineral = models.CharField(max_length=100, blank=False)
    status = models.ManyToManyField(Status, blank=True)

    def __str__(self):
        return self.name_of_the_mineral