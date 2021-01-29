from django.contrib import admin
from django.urls import path


urlpatterns = [

    path('admin/', admin.site.urls),

]


# from django.contrib import admin
# from django.urls import path
# from blog.admin import blog_site
# from bookstore.admin import bookstore_site

# urlpatterns = [

#     path('admin/', admin.site.urls), ## blogadmin as default
#     path('blogadmin/', blog_site.urls),
#     path('bookstore/', bookstore_site.urls),
# ]

# # admin.site.index_title = 'The Book Store'
# # admin.site.site_header = 'The Book Store Admin'
# # admin.site.site_title = 'Site Title Book Store'
