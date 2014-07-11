from django.conf.urls import url

from designer import views

urlpatterns = [
    url(r'^$', views.Designer_list.as_view(), name='list'),
	url(r'^(?P<designer_slug>[\w-]*)_(?P<pk>\d+)/$', views.Designer_profile.as_view(), name='profile'),
	url(r'^(?P<designer_slug>[\w-]*)_(?P<lookbook_slug>[\w-]*)_(?P<pk>\d+)/$', views.Lookbook_list.as_view(), name='lookbook'),
]



"""

from django.conf.urls import url

from designer import views
from oscar.core.loading import get_class

# Trying to do same for lookbook list
#lookbook_list_view = get_class('designer.views','LookbookListView')


urlpatterns = [
    url(r'^lookbooks/$',
                views.LookbookListView.as_view(),
                name='catalogue-lookbook-list'),     ##ADDED BY ME
]

#url(r'^$', views.GatewayView.as_view(), name='gateway')
"""