from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib import messages
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
    if obj != None and request.POST.get('action') == 'delete_selected':
      messages.add_message(request, messages.ERROR, (
        'Tell me. Are you really sure?'
      ))
    return True

  def has_module_permission(self, request):
    return True

blog_site = BlogAdminArea(name='BlogAdmin')

blog_site.register(models.Post, TestAdminPermissions)
blog_site.register(User)


# =============== POPULANDO FORM ==================== 
# If you are trying to set the queryset or (available options) for that field, then you can do the following

# def __init__(self, *args, **kwargs):
#     maker_id = kwargs.pop('maker_id')
#     super(OfferForm, self).__init__(*args, **kwargs)
#     maker = UserProfile.objects.get(id=maker_id)
#     self.fields['maker'].queryset = maker


# In may case, I wanted to set the initial or (default) value for that field. So, I had to pass an object not queryset

# def __init__(self, *args, **kwargs):
#     maker_id = kwargs.pop('maker_id')
#     super(OfferForm, self).__init__(*args, **kwargs)
#     maker = UserProfile.objects.get(id=maker_id)
#     self.fields['maker'].initial = maker.first()
# You can actually do both! set the queryset AND an initial value