
"""
import six

from django.shortcuts import render


from django.core.exceptions import ObjectDoesNotExist
from django.views import generic
from django.db.models import Q
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string

from oscar.core.loading import get_classes, get_model
from oscar.views import sort_queryset
from oscar.views.generic import ObjectLookupView


from django.utils.http import urlquote
from django.conf import settings
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
#from django.utils.translation import ugettext_lazy as _

from oscar.core.loading import get_class, get_model
from oscar.apps.catalogue.signals import product_viewed

from designer.models import Designer
from apps.catalogue.models import DesLookbook

class LookbookListView(generic.ListView):

    default_permissions = ['is_staff','partner.dashboard_access']
    #permissions_map = _map= {
        #'designer': (['is_staff'], ['partner.dashboard_access']),
        #}
    
    template_name = 'designer/lookbook_list.html'  ##sandbox/templates/designer
    model = DesLookbook
    context_object_name = 'lookbooks'
    
    def get_context_data(self, **kwargs):
            context = super(LookbookListView, self).get_context_data(**kwargs)
            return context
            #context['now'] = timezone.now()
"""