from django.contrib import admin
from . import models


admin.site.register(models.Author)
admin.site.register(models.News)
admin.site.register(models.Attachments)