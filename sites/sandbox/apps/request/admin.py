from django.contrib import admin

# Register your models here.

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from request.models import DesignerRequest

from django import forms
from request.forms import DesignerRequestForm 

class DesignerRequestAdmin(admin.ModelAdmin):
	form = DesignerRequestForm
	list_display = ('name','speciality','gender','description',) 
	list_display_links = ('name',) 
	list_filter = ('date_requested',)
	list_per_page = 50 
	ordering = ['-name'] 	

	# def get_form(self, request, **kwargs):
	# 	form = super(DesignerRequestAdmin, self).get_form(request, **kwargs)
	# 	form.current_user = request.user
	# 	return form
##now access the current user in forms.ModelForm by accessing self.current_user

admin.site.register(DesignerRequest, DesignerRequestAdmin) 