from django.conf.urls import url

from request import views

urlpatterns = [
    url(r'^$', views.Designer_Request.as_view(), name='designer-request'),
    url(r'^success/',views.Request_Success, name = 'request-success'),
]

