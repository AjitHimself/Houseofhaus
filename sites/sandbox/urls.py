from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf.urls.static import static

from oscar.app import shop
from oscar.views import handler500, handler404, handler403  # noqa

from apps.sitemaps import base_sitemaps


admin.autodiscover()

urlpatterns = [
    # Include admin as convenience. It's unsupported and you should
    # use the dashboard
    url(r'^admin/', include(admin.site.urls)),
    # i18n URLS need to live outside of i18n_patterns scope of the shop
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # include a basic sitemap
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.index', {
        'sitemaps': base_sitemaps}),
    
    url(r'^sitemap-(?P<section>.+)\.xml$',
        'django.contrib.sitemaps.views.sitemap', {'sitemaps': base_sitemaps}),
    # @ajit: URLS added for allauth access
    url(r'^accnt/', include('allauth.urls')),
    url(r'^relationships/', include('relationships.urls')),
]

# Prefix Oscar URLs with language codes
urlpatterns += i18n_patterns('',
    # Custom functionality to allow dashboard users to be created
    url(r'gateway/', include('apps.gateway.urls')),
    url(r'request/', include('apps.request.urls', namespace='request', app_name='request')),
    # @vivek: added new url for designer access on first page
    url(r'designer/', include('apps.designer.urls', namespace='designer', app_name='designer')),
    # @ajit: Payment gateway URL
    url(r'payzippy/', include('apps.payzippy.urls', namespace='payzippy', app_name='payzippy')),
    # @ajit: Relationships URL
    # url(r'relationships/', include('relationships.urls', namespace='relationships', app_name='relationships')),
    # Oscar's normal URLs
    url(r'', include(shop.urls)),

)

if settings.DEBUG:
    import debug_toolbar

    # Server statics and uploaded media
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    # Allow error pages to be tested
    urlpatterns += [
        url(r'^403$', handler403),
        url(r'^404$', handler404),
        url(r'^500$', handler500),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
