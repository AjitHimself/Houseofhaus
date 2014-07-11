
from oscar.apps.catalogue.app import CatalogueApplication as CoreCatalogueApplication

#from apps.catalogue.views import MyExtraView

from django.conf.urls import url

#from oscar.core.application import Application
from oscar.core.loading import get_class

from apps.catalogue.views import *

# @vivek: wiped out code over here bcoz it wasn't of any help
