from django.conf.urls import url

from designer import views

urlpatterns = [
    url(r'^$', views.Designer_list.as_view(), name='list'),
	url(r'^(?P<designer_slug>[\w-]*)_(?P<pk>\d+)/$', views.Designer_profile.as_view(), name='profile'),
	url(r'^(?P<designer_slug>[\w-]*)_(?P<lookbook_slug>[\w-]*)_(?P<pk>\d+)/$', views.Lookbook_list.as_view(), name='lookbook'),
]


