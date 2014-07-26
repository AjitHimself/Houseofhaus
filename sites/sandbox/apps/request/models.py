from django.utils.translation import ugettext_lazy as _
from datetime import datetime, date
from django.core.validators import RegexValidator

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from django.db import models
from oscar.core.compat import AUTH_USER_MODEL
#from oscar.core.compat import AUTH_USER_MODEL
#from oscar.apps.catalogue.models import Product

# Create your models here.


class DesignerRequest(models.Model):
   
	name = models.CharField(_('Name'), max_length=255, null=True, editable = False)

	email = models.EmailField(_('Email ID'), unique=True, null =True, editable = False)
		
	contact = models.CharField(validators=[RegexValidator(regex='^[0-9]{10}$', message='Enter a valid phone no.', code='nomatch')], max_length=10, null=True)

	
	Speciality_Choices = (('narrator', 'Narrator'),
		                  ('characterist','Characterist'),
		                  ('personalist','Personalist'),
		                  ('aspirant','Aspirant'),
		                  ('conceptualist','Conceptualist'),
		                  ('postmodernist','Postmodernist'),
		                  ('technician','Technician'),
		                  ('artisan','Artisan'),
		                  ('mixed', 'Mixed'),
		                  ('other','Other'),
						  )

	speciality = models.CharField(_('Speciality'), choices=Speciality_Choices,
	max_length=30,blank= True, null=True)
	
	date_requested = models.DateTimeField(_('Request Date'),auto_now_add=True, null=True)

	label = models.CharField(_('Label u belong to'), max_length=255,blank=True,null=True)

	description = models.TextField(_('Something about you'), blank= True)

	# def save(self, request, *args, **kwargs):

	# 	if not self.id:
	# 		self.name = request.user.username
	# 		self.email = request.user.email
	# 		super(DesignerRequest, self).save(*args, **kwargs)


	def __unicode__(self):
		return unicode(self.name)
       
	#class Meta:
		#verbose_name = _("")
		#verbose_name_plural = _("Order Notes")

	