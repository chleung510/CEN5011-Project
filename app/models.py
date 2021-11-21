"""
Definition of models.
"""

from django.db import models
#from django.contrib.gis.db import models

# Create your models here.
class Notice(models.Model):
    #id = models.AutoField(primary_key=True, default=0)
    noticeID = models.AutoField(primary_key=True)
    #noticeID =  models.CharField(max_length=10)
    heading= models.CharField(max_length=200)
    content= models.CharField(max_length=1000)
    #location = models.PointField(default=None, blank=True, null=True)
    def __str__(self):
        return self.heading
    
