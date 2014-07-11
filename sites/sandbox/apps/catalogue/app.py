
from oscar.apps.catalogue.app import CatalogueApplication as CoreCatalogueApplication

#from apps.catalogue.views import MyExtraView

from django.conf.urls import url

#from oscar.core.application import Application
from oscar.core.loading import get_class

from apps.catalogue.views import *

class CatalogueApplication(CoreCatalogueApplication):
	#extra_view = MyExtraView 
	name = 'catalogue'  # SINCE IN oscar.apps.catalogue.app name isn't given
	default_permissions = ['is_staff', ]

	lookbook_list_view = get_class('apps.catalogue.views',
								  'LookbookListView')
'''
	def get_urls(self):
		urls = [
			#url(r'^products/(?P<pk>\d+)/$',
			 #   self.product_createupdate_view.as_view(),
			  #  name='catalogue-product'),
			# Added URL for lookbook
			url(r'^lookbooks/$',
				self.lookbook_list_view.as_view(),
				name='catalogue-lookbook-list'),
		]
		return self.post_process_urls(urls)
'''

application = CatalogueApplication()
