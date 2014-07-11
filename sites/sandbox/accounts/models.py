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



# class Designer(models.Model):
# 	# This line  Links UserProfile to a User model instance.
# 	user = models.OneToOneField(AUTH_USER_MODEL, )


# 	# The additional attributes 
# 	email = models.EmailField('Email Address',max_length=250, unique=True,null=True)
# 	user_type= models.CharField(max_length=30, choices= {('S','Student'), 
# 	                                                                                 ('T','Teacher'),}, null=True )
# 	website = models.URLField(blank=True)
# 	picture = models.ImageField(upload_to='profile_images', blank=True)
# 	date_added=models.DateTimeField('Date Joined',auto_now_add=True,null=True)

# 	# Override the __unicode__() method to return out something meaningful!
# 	def __unicode__(self):
# 		return unicode(self.user)