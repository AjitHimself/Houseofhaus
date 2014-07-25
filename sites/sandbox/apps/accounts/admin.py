from django.contrib import admin

from accounts.models import *

class AccountsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','email','is_designer','date_joined')
    list_display_links = ('first_name','email','date_joined') 

# class DesignerAdmin(admin.ModelAdmin):
#     list_display = ('user','email','date_added')
#     list_display_links = ('user','email','date_added') 


admin.site.register(Users, AccountsAdmin)
#admin.site.register(Designer, DesignerAdmin)