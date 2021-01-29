from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
  fields = ['title', ('author', 'slug')]

admin.site.register(Post, PostAdmin)








# from django.contrib import admin
# import django.apps

# models = django.apps.apps.get_models()

# print(models)

# for model in models:
#   try:
#     admin.site.register(model)
#   except admin.sites.AlreadyRegistered:
#     pass

# admin.site.unregister(django.contrib.contenttypes.models.ContentType)

# # from django.contrib import admin
# # from . import models

# # models = django.apps.apps.get_models()

# # print(models)

# # class BlogAdminArea(admin.AdminSite):
# #   site_header = 'Blog Admin Area'

# # blog_site = BlogAdminArea(name='BlogAdmin')

