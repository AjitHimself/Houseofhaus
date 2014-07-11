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