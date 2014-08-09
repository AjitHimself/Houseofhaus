from django.contrib import admin

from accounts.models import *

class AccountsAdmin(admin.ModelAdmin):
    list_display = ('username','email','is_designer','is_staff','date_joined')
    list_display_links = ('username','email','date_joined') 

# @ajit: Didn't register this admin bcoz in Relationships admin did
#admin.site.register(Users, AccountsAdmin)