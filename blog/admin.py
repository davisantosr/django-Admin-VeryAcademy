from django.contrib import admin
from django.contrib.auth.models import User
from . import models

class BlogAdminArea(admin.AdminSite):
  site_header = 'Blog Admin - Custom'

class TestAdminPermissions(admin.ModelAdmin):
  def has_add_permission(self, request):
    if not request.user.is_superuser:
      return False
    return True

  def has_change_permission(self, request, obj=None) -> bool:
      # if request.user.groups.filter(name='nameofsomegroup').exists():
      #   return True
    return True

  def has_view_permission(self, request, obj=None):
    return True

  def has_delete_permission(self, request, obj=None):
    return True

  def has_module_permission(self, request):
    return True

blog_site = BlogAdminArea(name='BlogAdmin')

blog_site.register(models.Post, TestAdminPermissions)
blog_site.register(User)