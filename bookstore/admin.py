from django.contrib import admin

class BookstoreAdminArea(admin.AdminSite):
  site_header = 'Book Store Admin Area'

bookstore_site = BookstoreAdminArea(name='BookstoreAdmin')