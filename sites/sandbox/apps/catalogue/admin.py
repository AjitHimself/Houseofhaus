from __future__ import absolute_import
from six import with_metaclass
from django.contrib import admin
from django.db import models

from oscar.core.loading import get_model   #SEE ITS OTHER WAY TO IMPORT MODELS

from oscar.apps.catalogue.admin import *  # noqa

#from oscar.apps.catalogue.admin import AttributeInline, CategoryInline, ProductRecommendationInline
#from oscar.apps.catalogue.models import Product

from apps.catalogue.models import Product,DesLookbook
from apps.designer.models import Designer

ProductImage = get_model('catalogue', 'ProductImage')   #same as from apps.catalogue.models import ProductImage

Product = get_model('catalogue', 'Product')

##Snippet to use foo__object for list display in case of FK relations

def getter_for_related_field(name, admin_order_field=None, short_description=None):
    
    """
        Create a function that can be attached to a ModelAdmin to use as a list_display field, e.g:
        client__name = getter_for_related_field('client__name', short_description='Client')
    """
    related_names = name.split('__')
    def getter(self, obj):
        for related_name in related_names:
            obj = getattr(obj, related_name)
        return obj
    getter.admin_order_field = admin_order_field or name
    getter.short_description = short_description or related_names[-1].title().replace('_',' ')
    return getter


class RelatedFieldAdminMetaclass(type(admin.ModelAdmin)):
    """
        Metaclass used by RelatedFieldAdmin to handle fetching of related field values.
        We have to do this as a metaclass because Django checks that list_display fields are supported by the class.
    """
    def __new__(cls, name, bases, attrs):
        new_class = super(RelatedFieldAdminMetaclass, cls).__new__(cls, name, bases, attrs)

        for field in new_class.list_display:
            if '__' in field:
                setattr(new_class, field, getter_for_related_field(field))

        return new_class


class RelatedFieldAdmin(with_metaclass(RelatedFieldAdminMetaclass,admin.ModelAdmin)):
    """
        Version of ModelAdmin that can use related fields in list_display, e.g.:
        list_display = ('address__city', 'address__country__country_code')
    """
    def queryset(self, request):
        qs = super(RelatedFieldAdmin, self).queryset(request)

        # include all related fields in queryset
        select_related = [field.rsplit('__',1)[0] for field in self.list_display if '__' in field]

        # Include all foreign key fields in queryset.
        # This is based on ChangeList.get_query_set().
        # We have to duplicate it here because select_related() only works once.
        # Can't just use list_select_related because we might have multiple__depth__fields it won't follow.
        model = qs.model
        for field_name in self.list_display:
            try:
                field = model._meta.get_field(field_name)
            except models.FieldDoesNotExist:
                continue
            if isinstance(field.rel, models.ManyToOneRel):
                select_related.append(field_name)

        return qs.select_related(*select_related)





##### USAGE ####
#class FooAdmin(RelatedFieldAdmin):
#    # these fields will work automatically:
#    list_display = ('address__phone','address__country__country_code','address__foo')
#
#    # ... but you can also define them manually if you need to override short_description:
#    address__foo = getter_for_related_field('address__foo', short_description='Custom Name')



class DesLookbookAdmin(admin.ModelAdmin):
	list_display = ('name','designer') 
	list_display_links = ('name','designer',) 
	list_per_page = 50 
	ordering = ['-designer'] 
        filter_horizontal = ('products',)
        #inlines = [DesLookbookProductInline]

'''
class ProductAdmin(admin.ModelAdmin):
    list_display = ('get_title', 'upc', 'get_product_class', 'is_top_level',
                    'is_variant', 'attribute_summary',
                    'date_created')
	fieldsets = [
        (None, { 'fields': [('get_title', 'upc', 'get_product_class', 'is_top_level',
                    'is_variant', 'attribute_summary',
                    'date_created')] } ),
    ]
 
	prepopulated_fields = {"slug": ("title",)}
	inlines = [AttributeInline, CategoryInline, ProductRecommendationInline]
	
		def save_model(self, request, obj, form, change):
		if getattr(obj, 'designer', None) is None:
			obj.designer = request.user
		obj.save()
'''

class ProductImageAdmin(admin.ModelAdmin):
	product__parent = getter_for_related_field('product__parent', short_description='Parent Product')
	product__categories = getter_for_related_field('product__categories', short_description='Product Category')
	list_display = ('product','display_order','product__parent','product__categories',)
	list_filter = ('product__categories','product__product_class','product__date_created',)


"""
class ProductAdmin(admin.ModelAdmin):
	exclude=('video',)
"""
admin.site.register(DesLookbook, DesLookbookAdmin) 
#admin.site.register(Product, ProductAdmin)          #Model Product is already registered.
admin.site.register(ProductImage,ProductImageAdmin)  #Even though ProductImage is present in admin of oscar but it isn't registered with ProductImageAdmin 
#Its like: admin.site.register(ProductImage)




