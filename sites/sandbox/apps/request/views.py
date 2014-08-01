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

# PageTitleMixin, RegisterUserMixin = get_classes(
#     'customer.mixins', ['PageTitleMixin', 'RegisterUserMixin'])
# Dispatcher = get_class('customer.utils', 'Dispatcher')
# EmailAuthenticationForm, EmailUserCreationForm, OrderSearchForm = get_classes(
#     'customer.forms', ['EmailAuthenticationForm', 'EmailUserCreationForm',
#                        'OrderSearchForm'])
# PasswordChangeForm = get_class('customer.forms', 'PasswordChangeForm')
# ProfileForm, ConfirmPasswordForm = get_classes(
#     'customer.forms', ['ProfileForm', 'ConfirmPasswordForm'])
# UserAddressForm = get_class('address.forms', 'UserAddressForm')
# Order = get_model('order', 'Order')
# Line = get_model('basket', 'Line')
# Basket = get_model('basket', 'Basket')
# UserAddress = get_model('address', 'UserAddress')
# Email = get_model('customer', 'Email')
# ProductAlert = get_model('customer', 'ProductAlert')
# CommunicationEventType = get_model('customer', 'CommunicationEventType')

User = get_user_model()



class Designer_Request(FormView):
    template_name = 'request/designer_request.html'
    success_url = 'success/'    ##to redirect to the same url we can use success_url="."
    form_class = DesignerRequestForm


    # def save(self, request, obj, form, change):
    #     obj.name = self.request.user
    #     obj.email= self.cleaned_data['email']
    #     obj.save()


    def form_valid(self, form):
        print "IM IN FORM VALID"
        form.instance.name = self.request.user
        form.instance.email = self.request.user.email
        form.save()
        return super(Designer_Request, self).form_valid(form)



### We are using a simple view to direct the success url returned by 
def Request_Success(request):
    print "IM IN REQUEST SUCCESS"
    context = RequestContext(request)
    return render_to_response('request/success.html', {}, context)

