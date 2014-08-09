from django.db import models
from django.utils.translation import ugettext_lazy as _
from oscar.apps.customer.abstract_models import AbstractUser

from oscar.core.compat import AUTH_USER_MODEL

from oscar.models.fields import NullCharField, AutoSlugField

class Users(AbstractUser):

	username = models.CharField(max_length=50, null=True, unique=True)

	gender= models.CharField(max_length=30, choices= {('M','Male'), 
		('F','Female'),}, null=True, blank=True )

	is_designer = models.BooleanField(
		_('Is Designer'), default=False,
		help_text=_('Used in Partner and LookBook'),)

	proffesion = models.CharField(max_length=50, null=True, blank=True)
	website = models.URLField(max_length=255, null=True, blank=True)
	location = models.CharField(max_length=50, null=True, blank=True)

	twitter_link = models.CharField(max_length=255, null=True, blank=True)
	facebook_link = models.CharField(max_length=255, null=True, blank=True)
	instagram_link = models.CharField(max_length=255, null=True, blank=True)

	profile_pic = models.ImageField(upload_to='Accounts/Profile_pictures', blank=True, null= True)

