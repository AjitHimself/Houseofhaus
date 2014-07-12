from django.contrib import admin
from oscar.core.loading import get_model
from treebeard.admin import TreeAdmin

AttributeEntity = get_model('catalogue', 'AttributeEntity')
AttributeEntityType = get_model('catalogue', 'AttributeEntityType')
AttributeOption = get_model('catalogue', 'AttributeOption')
AttributeOptionGroup = get_model('catalogue', 'AttributeOptionGroup')
Category = get_model('catalogue', 'Category')
Option = get_model('catalogue', 'Option')
Product = get_model('catalogue', 'Product')
ProductAttribute = get_model('catalogue', 'ProductAttribute')
ProductAttributeValue = get_model('catalogue', 'ProductAttributeValue')
ProductCategory = get_model('catalogue', 'ProductCategory')
ProductClass = get_model('catalogue', 'ProductClass')
ProductImage = get_model('catalogue', 'ProductImage')
ProductRecommendation = get_model('catalogue', 'ProductRecommendation')

ProductFilter = get_model('catalogue', 'ProductFilter')


class AttributeValueInline(admin.TabularInline):
    model = ProductAttributeValue
    extra = 2

class ProductRecommendationInline(admin.TabularInline):
    model = ProductRecommendation
    fk_name = 'primary'


class CategoryInline(admin.TabularInline):
    model = ProductCategory
    extra = 1


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 2


class ProductClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'requires_shipping', 'track_stock')
    inlines = [ProductAttributeInline]

###########################################################
class ProductFilterInline(admin.TabularInline):
    model = ProductFilter

 #copied to sandbox.apps.catalogue.admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('get_title', 'upc', 'get_product_class','designer', 'is_top_level', 'is_variant', 'attribute_summary', 'date_created',)

    list_filter = ('designer',)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [AttributeValueInline,ProductFilterInline, CategoryInline, ProductRecommendationInline]
    
    
"""
    fieldsets = [
        (None, { 'fields': [('get_title', 'upc', 'get_product_class', 'is_top_level',
                    'is_variant', 'attribute_summary',
                    'date_created')] } ),
                     ]
"""
"""
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'designer', None) is None:
            obj.designer = request.user
        obj.save()
"""

class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'product_class', 'type')
    prepopulated_fields = {"code": ("name", )}


class OptionAdmin(admin.ModelAdmin):
    pass


class ProductAttributeValueAdmin(admin.ModelAdmin):
    list_display = ('product', 'attribute', 'value')


class AttributeOptionInline(admin.TabularInline):
    model = AttributeOption


class AttributeOptionGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'option_summary')
    inlines = [AttributeOptionInline, ]


class AttributeEntityAdmin(admin.ModelAdmin):
    list_display = ('name', )


class CategoryAdmin(TreeAdmin):
    pass


admin.site.register(ProductClass, ProductClassAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductAttribute, ProductAttributeAdmin)
admin.site.register(ProductAttributeValue, ProductAttributeValueAdmin)
admin.site.register(AttributeOptionGroup, AttributeOptionGroupAdmin)
admin.site.register(AttributeEntity, AttributeEntityAdmin)
admin.site.register(AttributeEntityType)
admin.site.register(Option, OptionAdmin)
#admin.site.register(ProductImage)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductCategory)
