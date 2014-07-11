from django.shortcuts import render
from django import forms

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from django.contrib.auth.decorators import login_required, user_passes_test

from request.forms import DesignerRequestForm 
from request.forms import *

from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django import http
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import logout as auth_logout, login as auth_login
from django.contrib.sites.models import get_current_site
from django.conf import settings

from oscar.core.loading import get_model
from oscar.views.generic import PostActionMixin
from oscar.apps.customer.utils import get_password_reset_url
from oscar.core.loading import get_class, get_profile_class, get_classes
from oscar.core.compat import get_user_model

#from . import signals

from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from designer.models import Designer
from catalogue.models import DesLookbook



User = get_user_model()


#The object list will always have the name 'object_list', if you want to change this 
#behaviour, you must pass in context_object_name as a keyword argument to the as_view() 
#in the url alongside model / paginate_by etc. 
#Or you must define it in your class if you are using the class to write views.

#What if my queryset / model returns no object. This case will raise a 404 error, 
#unless you pass in an allow_empty = True keyword into the as_view() 
#or define it in your class. 

class Designer_list(ListView):

    model= Designer
    #queryset = Designer.objects.filter(myfield="foo")
    # context_object_name = ""
    template_name = 'designer/list.html'
    #paginate_by = settings.OSCAR_PRODUCTS_PER_PAGE
    #enforce_paths = True


    def get_context_data(self, **kwargs):
        print self.kwargs
        print 'vivek'
        p = DesLookbook.objects.all()
        print p
        context = super(Designer_list, self).get_context_data(**kwargs)
        context['designers'] = Designer.objects.all()
        #context['designer'] =  Designer.objects.get(id=self.kwargs['pk'])
        # context['lookbooks'] = DesLookbook.objects.order_by('-designer')
        context['lookbooks'] = DesLookbook.objects.all()
        return context


class Designer_profile(DetailView):

    model= Designer
    template_name = 'designer/profile.html'

    # def get_object(self):
    #     if 'pk' in self.kwargs:
    #         self.designer = get_object_or_404(Designer, pk=self.kwargs['pk'])
        
    #     elif 'category_slug' in self.kwargs:
    #         # For SEO reasons, we allow chopping off bits of the URL. If that
    #         # happened, no primary key will be available.
    #         self.designer = get_object_or_404(
    #             Designer, slug=self.kwargs['designer_slug'])
    #     else:
    #         # If neither slug nor primary key are given, we show all products
    #         self.designer = None  

    def get_context_data(self, **kwargs):
        print self.kwargs
        n = self.kwargs['pk']
        print 'vivek'



        designer = Designer.objects.get(id=self.kwargs['pk'])
        print designer.date_joined 
        print designer.name
        print designer.profile_pic
        context = super(Designer_profile, self).get_context_data(**kwargs)
        context['designer']= designer
        return context


class Lookbook_list(ListView):

    model= Designer
    #queryset = Designer.objects.filter(myfield="foo")
    # context_object_name = ""
    template_name = 'designer/lookbook.html'
    #paginate_by = settings.OSCAR_PRODUCTS_PER_PAGE
    #enforce_paths = True


    def get_context_data(self, **kwargs):
        print self.kwargs
        print 'vivek'
        p = DesLookbook.objects.all()
        print p
        context = super(Designer_list, self).get_context_data(**kwargs)

        context['designers'] = Designer.objects.all()
        # context['lookbooks'] = DesLookbook.objects.order_by('-designer')
        context['lookbooks'] = DesLookbook.objects.all()
        return context


    # def get_categories(self):
    #     """
    #     Return a list of the current category and it's ancestors
    #     """
    #     return list(self.category.get_descendants()) + [self.category]

    # def get_summary(self):
    #     """
    #     Summary to be shown in template
    #     """
    #     return self.category.name if self.category else _('All products')

    # def get_context_data(self, **kwargs):
    #     context = super(ProductCategoryView, self).get_context_data(**kwargs)
    #     context['category'] = self.category
    #     context['summary'] = self.get_summary()
    #     return context

    # def get_queryset(self):
    #     qs = Product.browsable.base_queryset()
    #     if self.category is not None:
    #         categories = self.get_categories()
    #         qs = qs.filter(categories__in=categories).distinct()
    #     return qs





### We are using a simple view to direct the success url returned by 
def Request_Success(request):
    context = RequestContext(request)
    return render_to_response('request/success.html', {}, context)
