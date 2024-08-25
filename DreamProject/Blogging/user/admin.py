from django.contrib import admin

# Register your models here.
from .models import *


class contactAdmin(admin.ModelAdmin):
    list_display = ("name", "mobile", "email", "message", "address")

admin.site.register(contact, contactAdmin)


class categoryAdmin(admin.ModelAdmin):
    list_display = ("id", "cname", "cimage", "cdate")

admin.site.register(category, categoryAdmin)


class profileAdmin(admin.ModelAdmin):
    list_display = ("name", "dob", "gender", "mobile", "email", "password", "profession", "college", "pic")

admin.site.register(profile, profileAdmin)

class blogdetailAdmin(admin.ModelAdmin):
    list_display = ("authorid", "blogcategory", "topic", "description", "attachment", "thumbnail", "bdate")

admin.site.register(blogdetail, blogdetailAdmin)
