from django.db import models

# Create your models here.
class Banks(models.Model):
    """Model for banks"""
    name = models.CharField(max_length=1000)
    def __str__(self):
        return str(self.name)

class Branches(models.Model):
    """Model for branches with foreign key to model Banks"""
    ifsc = models.CharField(max_length=11)
    bank_id = models.ForeignKey(Banks,to_field='id',on_delete=models.CASCADE,related_name='bankid')
    branch = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=60)
    state = models.CharField(max_length=35)
    def __str__(self):
        return self.ifsc