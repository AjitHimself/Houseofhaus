import string
import random
from six.moves.urllib import parse

from django import forms

import datetime

from django.conf import settings
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.models import get_current_site
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import pgettext_lazy

from oscar.core.loading import get_profile_class, get_class, get_model
from oscar.core.compat import get_user_model, existing_user_fields
from oscar.apps.customer.utils import get_password_reset_url, normalise_email
from oscar.core.validators import password_validators

from request.models import DesignerRequest
from request.admin import *


User = get_user_model()

class DesignerRequestForm(forms.ModelForm):

    name = forms.CharField(label =_('Your Boutiques Name'),required = False)
    #name = forms.CharField(label =_('Your name'), help_text="Please enter your name",widget=forms.HiddenInput())

    email = forms.EmailField(label=_('Email address'),required = False)
    #email = forms.EmailField(label=_('Email address'),widget=forms.HiddenInput())
    #gender = forms.CharField(label='Select your gender',help_text="No size limit")
    #label = forms.CharField(label = _('Do u belong to any label'), blank=True, max_length=128, help_text="Please enter your name")
    
    #profile_pic = forms.ImageField(label=_('Your pic'),blank= True)

    #description = forms.TextField(_('Tell us something about u'))
    
    date_requested=forms.DateTimeField(widget=forms.HiddenInput(),help_text='Submission Date',initial=datetime.datetime.now())
    
    # password1 = forms.CharField(
    #     label=_('Password'), widget=forms.PasswordInput,
    #     validators=password_validators)
    # password2 = forms.CharField(
    #     label=_('Confirm password'), widget=forms.PasswordInput)

    # redirect_url = forms.CharField(
    #     widget=forms.HiddenInput, required=False)

    class Meta:
        model = DesignerRequest
        fields = ('name', 'email','contact','speciality','date_requested','label','description',) # tuple

    def clean_email(self):
        email = normalise_email(self.cleaned_data['email'])
        if User._default_manager.filter(email=email).exists():
            raise forms.ValidationError(_("A request from this email address is received. We will contact u soon."))
        return email

    # def save(self,user, commit=True, *args, **kwargs):
    #     var = super(DesignerRequestForm, self).save(commit=False,*args, **kwargs)
    #     var.name = user
    #     if commit:
    #         var.save()
    #     return var

    #  #form stuff
    # def save(self,*args, **kwargs):
    #     self.name = self.current_user
    #     self.email = self.cleaned_data['email']
    #     super(DesignerRequestForm, self).save(*args, **kwargs)


    

    # def __init__(self, host=None, *args, **kwargs):
    #     self.host = host
    #     super(EmailUserCreationForm, self).__init__(*args, **kwargs)

    
        #form_data = self.cleaned_data
        #Do something here
   
    # def clean_redirect_url(self):
    #     url = self.cleaned_data['redirect_url'].strip()
    #     if not url:
    #         return settings.LOGIN_REDIRECT_URL
    #     host = parse.urlparse(url)[1]
    #     if host and self.host and host != self.host:
    #         return settings.LOGIN_REDIRECT_URL
    #     return url

    # def save(self, commit=True):
    #     user = super(EmailUserCreationForm, self).save(commit=False)
    #     user.set_password(self.cleaned_data['password1'])

    #     if 'username' in [f.name for f in User._meta.fields]:
    #         user.username = generate_username()
    #     if commit:
    #         user.save()
    #     return user