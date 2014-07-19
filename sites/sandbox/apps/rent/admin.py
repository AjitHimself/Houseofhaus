from django.contrib import admin


#from oscar.apps.catalogue.models import Product

from apps.rent.models import Rent


class RentAdmin(admin.ModelAdmin):
	list_display = ('stock_record','customer','period', 'start_date', 'end_date')
	list_display_links = ('stock_record',) 
	list_filter = ('customer',)
	readonly_fields=('start_date','end_date')


admin.site.register(Rent, RentAdmin) 