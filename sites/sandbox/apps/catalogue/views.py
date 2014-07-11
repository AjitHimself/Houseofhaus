import six

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

from apps.catalogue.models import DesLookbook

def filter_lookbooks(queryset, user):
    """
    Restrict the queryset to products the given user has access to.
    A staff user is allowed to access all Products.
    A non-staff user is only allowed access to a product if they are in at
    least one stock record's partner user list.
    """
    if user.is_staff:
        return queryset

    return queryset.filter(stockrecords__partner__users__pk=user.pk).distinct()


class LookbookListView(generic.ListView):
    
    template_name = 'dashboard/catalogue/lookbook_list.html'
    model = DesLookbook
    context_object_name = 'lookbooks'

    def get_context_data(self, **kwargs):
        context = super(LookbookListView, self).get_context_data(**kwargs)
        return context

    def filter_queryset(self, queryset):
        """
        Apply any filters to restrict the products that appear on the list
        """
        return filter_lookbooks(queryset, self.request.user)

    # def get_queryset(self):
    #     """
    #     Build the queryset for this list
    #     """
    #     queryset = DesLookbook.objects.base_queryset()
    #     queryset = self.filter_queryset(queryset)
    #     queryset = self.apply_search(queryset)
    #     queryset = self.apply_ordering(queryset)

    #     return queryset
# -----------------------------------------------------------------------------------

