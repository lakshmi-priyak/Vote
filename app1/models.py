from django.db import models
from datetime import date

# Create your models here.
class Vote(models.Model):
    name = models.CharField(max_length = 200)
    dob = models.DateField()

    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month , today.day) < (self.dob.month , self.dob.day))
    
    def iseligible(self):
        return self.age() > 18