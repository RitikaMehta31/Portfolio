from django.db import models

# Create your models here.
class Project(models.Model):
	name=models.CharField(max_length=120)
	description=models.TextField(max_length=125)
	slug=models.SlugField(unique=True,default=1)
	image=models.ImageField(upload_to='project/images',null=True,blank=True)
	url=models.URLField(blank=True)

	def __str__ (self):
		return self.name