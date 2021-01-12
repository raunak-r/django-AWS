from django.contrib import admin

from .models import *


class ModelS3Admin(admin.ModelAdmin):
	list_display = [field.name for field in ModelS3._meta.fields]
	list_per_page = 20

	class Meta:
		model = ModelS3
admin.site.register(ModelS3, ModelS3Admin)
