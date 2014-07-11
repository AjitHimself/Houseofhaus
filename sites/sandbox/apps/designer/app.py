"""
from django.conf.urls import url, include

from oscar.core.application import Application
from oscar.core.loading import get_class

from apps.catalogue.models import *

from oscar.apps.catalogue.views import ProductDetailView,ProductCategoryView,RangeDetailView
from oscar.apps.offer.views import RangeDetailView

class DesignerApplication(Application):
    name = 'designer'
    #detail_view = get_class('catalogue.views', 'ProductDetailView')
    #category_view = get_class('catalogue.views', 'ProductCategoryView')
    #range_view = get_class('offer.views', 'RangeDetailView')

    def get_urls(self):
        urls = [
            url(r'page-redirect/(?P<page_promotion_id>\d+)/$',
                self.record_click_view.as_view(model=PagePromotion),
                name='page-click'),
            url(r'keyword-redirect/(?P<keyword_promotion_id>\d+)/$',
                self.record_click_view.as_view(model=KeywordPromotion),
                name='keyword-click'),
            url(r'^$', self.home_view.as_view(), name='home'),
        ]
        return self.post_process_urls(urls)


application = PromotionsApplication()


