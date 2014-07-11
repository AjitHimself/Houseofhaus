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
        form.instance.name = self.request.user
        form.instance.email = self.request.user.email
        form.save()
        return super(Designer_Request, self).form_valid(form)



### We are using a simple view to direct the success url returned by 
def Request_Success(request):
    context = RequestContext(request)
    return render_to_response('request/success.html', {}, context)


"""
@login_required
def designer_request(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = DesignerRequestForm(request.POST, request.FILES)

        if form.is_valid():
            # This time we cannot commit straight away.
            # Not all fields are automatically populated!
            n = form.save(commit=False)

            # Retrieve the associated topic object so we can add it.
            # Wrap the code in a try block - check if the topic actually exists!
            try:
                pg = Page.objects.get(title=topic_name)
                
                #putting this new note under the topic; remember note is a field in Note class
                n.note = pg



            except Page.DoesNotExist:
                # If we get here, the topic does not exist.
                # We render the add_note.html template without a context dictionary.
                # This will trigger the red text to appear in the template!
                return render_to_response('book/add_note.html', {}, context)

            # Also, create a default value for the number of views.
            n.likes = 0
            if 'picture' in request.FILES:
                n.picture= request.FILES['picture']

            if 'file' in request.FILES:
                n.file= request.FILES['file']
            # With this, we can then save our new model instance.
            n.save()

            # Now that the page is saved, display what u want.
            return HttpResponseRedirect('')

        else:
            print form.errors

    else:
        form = DesignerRequestForm()

    return render_to_response('request/designer_request.html', {'form':form},context)




class AccountAuthView(RegisterUserMixin, generic.TemplateView):
    
    # This is actually a slightly odd double form view that allows a customer to
    # either login or register.

    template_name = 'customer/login_registration.html'
    login_prefix, registration_prefix = 'login', 'registration'
    login_form_class = EmailAuthenticationForm
    registration_form_class = EmailUserCreationForm
    redirect_field_name = 'next'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return http.HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        return super(AccountAuthView, self).get(
            request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        ctx = super(AccountAuthView, self).get_context_data(*args, **kwargs)
        if 'login_form' not in kwargs:
            ctx['login_form'] = self.get_login_form()
        if 'registration_form' not in kwargs:
            ctx['registration_form'] = self.get_registration_form()
        return ctx

    def post(self, request, *args, **kwargs):
        # Use the name of the submit button to determine which form to validate
        if u'login_submit' in request.POST:
            return self.validate_login_form()
        elif u'registration_submit' in request.POST:
            return self.validate_registration_form()
        return http.HttpResponseBadRequest()

    # LOGIN

    def get_login_form(self, bind_data=False):
        return self.login_form_class(
            **self.get_login_form_kwargs(bind_data))

    def get_login_form_kwargs(self, bind_data=False):
        kwargs = {}
        kwargs['host'] = self.request.get_host()
        kwargs['prefix'] = self.login_prefix
        kwargs['initial'] = {
            'redirect_url': self.request.GET.get(self.redirect_field_name, ''),
        }

        if bind_data and self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs


###################################################################################
    def validate_login_form(self):
        form = self.get_login_form(bind_data=True)
        if form.is_valid():
            user = form.get_user()

            # Grab a reference to the session ID before logging in
            old_session_key = self.request.session.session_key

            auth_login(self.request, form.get_user())

            # Raise signal robustly (we don't want exceptions to crash the
            # request handling). We use a custom signal as we want to track the
            # session key before calling login (which cycles the session ID).
            signals.user_logged_in.send_robust(
                sender=self, request=self.request, user=user,
                old_session_key=old_session_key)

            msg = self.get_login_success_message(form)
            messages.success(self.request, msg)

            url = self.get_login_success_url(form)
            return http.HttpResponseRedirect(url)

        ctx = self.get_context_data(login_form=form)
        return self.render_to_response(ctx)

    def get_login_success_message(self, form):
        return _("Welcome back")

    def get_login_success_url(self, form):
        redirect_url = form.cleaned_data['redirect_url']
        if redirect_url:
            return redirect_url

        # Redirect staff members to dashboard as that's the most likely place
        # they'll want to visit if they're logging in.
        if self.request.user.is_staff:
            return reverse('dashboard:index')

        return settings.LOGIN_REDIRECT_URL

    # REGISTRATION

    def get_registration_form(self, bind_data=False):
        return self.registration_form_class(
            **self.get_registration_form_kwargs(bind_data))

    def get_registration_form_kwargs(self, bind_data=False):
        kwargs = {}
        kwargs['host'] = self.request.get_host()
        kwargs['prefix'] = self.registration_prefix
        kwargs['initial'] = {
            'redirect_url': self.request.GET.get(self.redirect_field_name, ''),
        }
        if bind_data and self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
            })
        return kwargs

    def validate_registration_form(self):
        form = self.get_registration_form(bind_data=True)
        if form.is_valid():
            self.register_user(form)

            msg = self.get_registration_success_message(form)
            messages.success(self.request, msg)

            url = self.get_registration_success_url(form)
            return http.HttpResponseRedirect(url)

        ctx = self.get_context_data(registration_form=form)
        return self.render_to_response(ctx)

    def get_registration_success_message(self, form):
        return _("Thanks for registering!")

    def get_registration_success_url(self, form):
        return settings.LOGIN_REDIRECT_URL

"""