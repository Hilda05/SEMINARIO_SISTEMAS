from django.db import models

# Create your models here.
class usuario(models.Model):
	Nick=models.CharField(max_length=100)
	Email=models.EmailField(max_length=100)
	Password=models.CharField(max_length=20)

	def __unicode__(self):
		return "%s "%(self.Nick)
