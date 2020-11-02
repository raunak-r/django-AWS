from django.db import models
from django.conf import settings

class ModelS3(models.Model):
	# id created by db
	username = models.CharField(max_length=20, null=False, unique=True)
	attachments = models.FileField(null=True, blank=True, upload_to=settings.MEDIAFILES_LOCATION)
	updated_date = models.DateTimeField(auto_now=True)
	created_date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.username
