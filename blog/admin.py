from django.contrib import admin
from . import models

import django.apps

# models = django.apps.apps.get_models() # Getting all models from the application
# registering models in a for loop
# for model in models:
#   try:
#     admin.site.register(model)
#   except admin.sites.AlreadyRegistered:
#     pass



class BlogAdminArea(admin.AdminSite):
  site_header = 'Blog Admin Area'
  login_template = 'blog/admin/login.html'

blog_site = BlogAdminArea(name='BlogAdmin')

blog_site.register(models.Post)