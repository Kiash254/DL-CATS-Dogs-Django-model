from django.db import models

# Create your models here.
from django.db import models

class YourData(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField(upload_to='images')
    
    def __str__(self):
        return self.field1
    
