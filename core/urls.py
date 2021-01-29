from django.contrib import admin
from django.urls import path
from blog.admin import blog_site

urlpatterns = [
    path('blogadmin/', blog_site.urls),
    path('admin/', admin.site.urls),
]

# admin.site.index_title = 'The Book Store'
# admin.site.site_header = 'The Book Store Admin'
# admin.site.site_title = 'Site Title Book Store'
