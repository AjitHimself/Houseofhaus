from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from datetime import datetime, date

from django.db import models
from oscar.core.compat import AUTH_USER_MODEL

from oscar.models.fields import NullCharField, AutoSlugField

#from oscar.apps.catalogue.models import Product

# Create your models here.

class Designer(models.Model):
   
	name = models.CharField(_('Name'), max_length=255,editable= False, null=True)
	designer = models.ForeignKey(AUTH_USER_MODEL, limit_choices_to ={'is_designer': True}, verbose_name=_("Designer Email"),null=True, blank=True, unique = True)
	#first_name = models.CharField(_('First name'), max_length=255, blank=True, null=True)
	#last_name = models.CharField(_('Last name'), max_length=255, blank=True, null= True)
	
	slug = models.SlugField(_('Slug'), max_length=255,editable=False)

	gender= models.CharField(max_length=30, choices= {('Male','Male'), 


	                                                                                 ('Female','Female'),}, null=True )
	#email = models.EmailField(_('Email ID'), unique=True, null =True)
	date_joined = models.DateTimeField(_('Date joined'),auto_now_add=True, null=True)

	profile_pic = models.ImageField(upload_to='Designer/Profile', blank=True, null= True)
	
         
	#class Meta:
		#verbose_name = _("")
		#verbose_name_plural = _("Order Notes")

	def save(self,*args, **kwargs):

		#if not self.id:
			super(Designer, self).save(*args,**kwargs)
			full_name = self.designer.first_name + " " + self.designer.last_name
			self.name = full_name
			self.slug = self.designer.first_name + "-" + self.designer.last_name
			super(Designer, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('designer:profile',kwargs={'designer_slug': self.slug, 'pk': self.id})

	def __unicode__(self):
		return unicode(self.name)


class DesPostCategory(models.Model):
	designer = models.ForeignKey(Designer, related_name='desig')
	name = models.CharField(max_length=30, default='default')
	date_created = models.DateTimeField(_('Date created'),auto_now_add=True, null=True)


	class Meta:
		unique_together = ("designer", "name")
		verbose_name = _("Post Category")
		verbose_name_plural = _("Post Categories")

	def __unicode__(self):
		return unicode(self.name)



class DesignerPost(models.Model):

	category = models.ForeignKey(DesPostCategory, related_name="categ", null=True)

	name = models.CharField(_('Name'), max_length=30, unique=True)
	
	designer = models.ForeignKey('Designer', related_name="des",null=True)

	post_status = models.CharField(_('Post Status'), max_length=30,blank=True)

	description = models.TextField()
	
	date_created = models.DateTimeField(_('Date created'),auto_now_add=True, null=True)

	last_edited = models.DateTimeField(_('Last edited'),auto_now_add=True, null=True)



	class Meta:
		verbose_name = _("Designer Post")
		verbose_name_plural = _("Designer Posts")

	def __unicode__(self):
		post_description ='%s: %s' % (self.designer, self.name)
		return unicode(post_description)	

	# def save(self, request, *args, **kwargs):
	# 	self.name = request.user.username
	# 	self.email = request.user.email
	# 	super(DesignerRequest, self).save(*args, **kwargs)

   # def save(self, request, obj, form, change):
    #     obj.name = self.request.user
    #     obj.email= self.cleaned_data['email']
    #     obj.save()


class DesPostImage(models.Model):
	post = models.ForeignKey(DesignerPost, related_name='postimage')
	image = models.ImageField(upload_to='Designer/Post/Images', blank=True, null= True)


class DesVideoUrl(models.Model):
	post = models.ForeignKey(DesignerPost, related_name='postvideo')
	video_url = models.URLField(blank=True)
	



		# def save(self, request, *args, **kwargs):
	# 	if not self.id:
	# 		self.date_created = self.last_edited + 
	# 		self.email = request.user.email
	# 		super(DesignerRequest, self).save(*args, **kwargs)

"""
class DesLookbook(models.Model):
    
	designer= models.ForeignKey('Designer', verbose_name=_("Designer"),null=True, blank=True)
    
	name= models.CharField(_("Lookbook name"),max_length=128,null=True,unique= True)

	products= models.ManyToManyField(Product, verbose_name=_("Product"), related_name= 'des_product', null=True,blank=True)



	description= models.TextField(_("Message"))

	class Meta:
		verbose_name = _("Designer Lookbook")
		verbose_name_plural = _("Designer Lookbooks")

	def __unicode__(self):
		return unicode(self.name)

"""



