from django.conf.urls import url, include

from oscar.core.loading import get_class

from oscar.apps.dashboard.app import DashboardApplication as CoreDashboardApplication 
from apps.dashboard.designer.app import application as designer_app 



class DashboardApplication(CoreDashboardApplication ):
    """    
    name = 'dashboard'
    permissions_map = {
        'index': (['is_staff'], ['partner.dashboard_access']),
        'catalogue-lookbook-list': (['is_staff'], ['partner.dashboard_access']),
    }

    lookbook_list_view = get_class('catalogue.views','LookbookListView')
    index_view = get_class('dashboard.views', 'IndexView')
    reports_app = get_class('dashboard.reports.app', 'application')
    orders_app = get_class('dashboard.orders.app', 'application')
    users_app = get_class('dashboard.users.app', 'application')
    catalogue_app = get_class('dashboard.catalogue.app', 'application')
    promotions_app = get_class('dashboard.promotions.app', 'application')
    pages_app = get_class('dashboard.pages.app', 'application')
    partners_app = get_class('dashboard.partners.app', 'application')
    offers_app = get_class('dashboard.offers.app', 'application')
    ranges_app = get_class('dashboard.ranges.app', 'application')
    reviews_app = get_class('dashboard.reviews.app', 'application')
    vouchers_app = get_class('dashboard.vouchers.app', 'application')
    comms_app = get_class('dashboard.communications.app', 'application')
    """
    designer_app = designer_app 

    def get_urls(self):
        urls = [
            url(r'^$', self.index_view.as_view(), name='index'),
            #url(r'^lookbooks/$', self.lookbook_list_view.as_view(), name='catalogue-lookbook-list'),
            url(r'^catalogue/', include(self.catalogue_app.urls)),
            url(r'^reports/', include(self.reports_app.urls)),
            url(r'^orders/', include(self.orders_app.urls)),
            url(r'^users/', include(self.users_app.urls)),
            url(r'^content-blocks/', include(self.promotions_app.urls)),
            url(r'^pages/', include(self.pages_app.urls)),
            url(r'^partners/', include(self.partners_app.urls)),
            url(r'^offers/', include(self.offers_app.urls)),
            url(r'^ranges/', include(self.ranges_app.urls)),
            url(r'^reviews/', include(self.reviews_app.urls)),
            url(r'^vouchers/', include(self.vouchers_app.urls)),
            url(r'^comms/', include(self.comms_app.urls)),

            url(r'^designer/', include(self.designer_app.urls)), 
            
        ]
        return self.post_process_urls(urls)


application = DashboardApplication()
