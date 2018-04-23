from django.db import models

# Create your models here.
class Info(models.Model):
	name = models.CharField(max_length=20)
	birthday = models.CharField(max_length=20)
	age = models.DecimalField(max_digits=3, decimal_places=0)
	
	def __str__(self):
		return self.name