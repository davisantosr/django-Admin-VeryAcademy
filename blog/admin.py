from django.contrib import admin
from . import models

class BlogAdminArea(admin.AdminSite):
  site_header = 'Blog Admin Area'

blog_site = BlogAdminArea(name='BlogAdmin')

blog_site.register(models.Post)
admin.site.register(models.Post)