from django.contrib import admin
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import RequestContext

from apps.catalogue.models import Product
from apps.catalogue.models import DesLookbook
from designer.models import Designer, DesignerPost, DesPostImage, DesPostCategory, DesVideoUrl

from oscar.core.compat import AUTH_USER_MODEL
from fk_listdisplay import *

from accounts.models import Users

# Register your models here.

class DesLookbookInline(admin.TabularInline):
	model = DesLookbook
	filter_vertical = ('products',)
	extra=0


class DesignerAdmin(admin.ModelAdmin):
	user__email = getter_for_related_field('designer__email', short_description='Designer Email-id')
	readonly_fields=('name',)
	list_display = ('name','user__email','date_joined') 
	list_display_links = ('name','date_joined') 
	list_filter = ('date_joined',)
	list_per_page = 50 
	ordering = ['-name'] 	
	inlines = [DesLookbookInline]


class PostImageInline(admin.TabularInline):
    model = DesPostImage
    extra = 3

class PostVideoInline(admin.TabularInline):
    model = DesVideoUrl
    extra = 3


class DesPostAdmin(admin.ModelAdmin):
	list_display = ('name','designer','category','post_status','date_created')
	#readonly_fields=('designer',)
	list_filter = ('designer','date_created',)
	list_display_links = ('name','category',) 
	ordering = ['-name'] 
	inlines = [ PostImageInline,PostVideoInline,]

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if not request.user.is_superuser:
			if db_field.name == "category":
			#full_name = request.user.first_name + " " + request.user.last_name
				var = Designer.objects.get(designer=request.user)
				kwargs["queryset"] = DesPostCategory.objects.filter(designer=var)

			if db_field.name == "designer":
				var = Designer.objects.get(designer=request.user)
				kwargs["queryset"] = Designer.objects.filter(designer=var)

		else:
			if db_field.name == "category":
				kwargs["queryset"] =DesPostCategory.objects.all()
			if db_field.name == "designer":
				kwargs["queryset"] =Designer.objects.all()
		return super(DesPostAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


 # def formfield_for_foreignkey(self, db_field, request, **kwargs):
 #        if not request.user.is_superuser:
 #            if db_field.name == "catagory":
 #                shop=Shop.objects.get(username=request.user.username)
 #                kwargs["queryset"] = Catagory.objects.filter(shop=shop)
 #        else:
 #            kwargs["queryset"] = Catagory.objects.all()
 #        return super(GoodsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


"""
1. request.user will be returning the email field while the designer returns the full name as it retur
ns the self.name which is actually fullname

2. normally we will logged in via admin itself, then user will be admin itself

3. so this solution is better only if we giving access via admin.
4. Better go for modelchoicefield in form.py
"""
class DesPostCategoryAdmin(admin.ModelAdmin):
	list_display = ('name','designer','date_created')
	list_filter = ('designer','date_created',)
	list_display_links = ('name',) 


"""
class DesLookbookProductInline(admin.TabularInline):
	model = DesLookbookProduct
"""	
"""
class DesLookbookAdmin(admin.ModelAdmin):
	list_display = ('name','designer') 
	list_display_links = ('name','designer',) 
	list_per_page = 50 
	ordering = ['-designer'] 
        filter_horizontal = ('products',)
        #inlines = [DesLookbookProductInline]
"""


admin.site.register(Designer) 
admin.site.register(DesignerPost, DesPostAdmin) 
admin.site.register(DesPostCategory, DesPostCategoryAdmin) 
#admin.site.register(DesLookbook, DesLookbookAdmin) 

