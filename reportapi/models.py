from django.db import models

# Create your models here.

class Report(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, blank=True, default='')
    source_link = models.CharField(max_length=500, blank=True, default='')
    report_files = models.FileField(upload_to = "mining-files", blank=True)
    
    def __str__(self):
        return f'{self.title}'
