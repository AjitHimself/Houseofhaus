from django.conf.urls import url

from oscar.core.application import Application
from oscar.core.loading import get_class


class DesignerApplication(Application):
    name = None

    default_permissions = ['is_staff', ]
    permissions_map = _map = {
        'catalogue-product': (['is_staff'], ['partner.dashboard_access']),
        'catalogue-product-create': (['is_staff'],
                                     ['partner.dashboard_access']),
        'catalogue-product-list': (['is_staff'], ['partner.dashboard_access']),
        # # added permission for lookbook-list
        # 'catalogue-lookbook-list': (['is_staff'], ['partner.dashboard_access']),
        # # ----------------------------------
        'catalogue-product-delete': (['is_staff'],
                                     ['partner.dashboard_access']),
        'catalogue-product-lookup': (['is_staff'],
                                     ['partner.dashboard_access']),
    }

    
    lookbook_list_view = get_class('apps.dashboard.designer.views',
                                  'LookbookListView')
    
   

    def get_urls(self):
        urls = [            
            url(r'^lookbooks/$',
                self.lookbook_list_view.as_view(),
                name='catalogue-lookbook-list'),

        ]
        return self.post_process_urls(urls)


application = DesignerApplication()
