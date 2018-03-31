from django.db import models
from django.utils import  timezone

# Create your models here.

class Comment(models.Model):
	name = models.CharField(max_length=200)
	comment = models.TextField()
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return '<Name: {}, ID: {}>'.format(self.name, self.id)
