from django.contrib import admin
from .models import Post
from django import forms
from .models import Post



class PostForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super(PostForm, self).__init__(*args, **kwargs)

    self.fields['title'].help_text= 'New Help Text'

    class Meta:
      model = Post
      exclude = ('slug',)


class PostFormAdmin(admin.ModelAdmin):
  form = PostForm

admin.site.register(Post, PostFormAdmin)







# ========================================================
# from django.contrib import admin

# from .models import Post

# TEXT = 'This is where you put some title and define the author'

# class PostAdmin(admin.ModelAdmin):
#   fieldsets = (
#     ('Section A', {
#       'fields': ('title', 'author',),
#       'description': '%s' % TEXT,
#     }),

#     ('Section B', {
#       'fields': ('slug',),
#       'classes': ('collapse',),
#     }),
#   )



# admin.site.register(Post, PostAdmin)


# ============================================================


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




# =====================================================

# # from django.contrib import admin
# # from . import models

# # models = django.apps.apps.get_models()

# # print(models)

# # class BlogAdminArea(admin.AdminSite):
# #   site_header = 'Blog Admin Area'

# # blog_site = BlogAdminArea(name='BlogAdmin')


# =======================================================