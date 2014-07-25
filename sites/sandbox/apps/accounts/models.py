from django.db import models
from django.utils.translation import ugettext_lazy as _
from oscar.apps.customer.abstract_models import AbstractUser

from oscar.core.compat import AUTH_USER_MODEL

from django.contrib.auth.models import User




class Users(AbstractUser):
	is_designer = models.BooleanField(
		_('Is Designer'), default=False,
		help_text=_('Designates whether this user should be treated as '
					'Designer. Used in Partner and LookBook'),)


