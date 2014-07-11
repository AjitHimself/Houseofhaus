from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from django.db import models
from designer.models import Designer
from oscar.apps.catalogue.abstract_models import AbstractProduct


class Product(AbstractProduct): 
    
	designer= models.ForeignKey(Designer,verbose_name=_("Designer"),null=True, blank=True, related_name='products')     
	
	video =models.FileField(upload_to='Product_videos',blank=True,null=True)     

	on_rent =models.BooleanField(_("Currently on rent?"), default=False,help_text=_("This flag indicates if this product is on rent at the moment it will be used to get the rent-price in the basket model and save it as stock_info before product is being put in a line")) 

	rent_count= models.IntegerField(_("No. of times product has been rented"),null=True,default=0)     

	#deslookbook= models.ForeignKey(DesLookbook,verbose_name=_("Designer Lookbook"),null=True,blank=True)


class DesLookbook(models.Model):
    
	designer= models.ForeignKey(Designer, verbose_name=_("Designer"),null=True, blank=True, related_name='lookbooks')
    
	name= models.CharField(_("Lookbook name"),max_length=128,null=True,unique= True)

	products= models.ManyToManyField(Product, verbose_name=_("Product"), related_name= 'lookbooks', null=True,blank=True)

	description= models.TextField(_("Message"))

	slug = models.SlugField(_('Slug'), max_length=255,editable=True, null=True)

	class Meta:
		verbose_name = _("Designer Lookbook")
		verbose_name_plural = _("Designer Lookbooks")

	def get_absolute_url(self):
		designer_slug= self.designer.slug 
		return reverse('designer:lookbook',kwargs={'designer_slug':designer_slug,'lookbook_slug': self.slug, 'pk': self.id, })

	def __unicode__(self):
		return unicode(self.name)



from oscar.apps.catalogue.models import *  #

"""
class DesLookbookProduct(models.Model):
     
	deslookbook= models.ForeignKey(DesLookbook, verbose_name=_("Deslookbook"), related_name= 'des lookbook', null=True,blank=True)

	products= models.ForeignKey(Product, verbose_name=_("Product"), related_name= 'des product', null=True,blank=True)

	
	order= models.PositiveIntegerField(_('Order'), default=0)

	class Meta:
		verbose_name = _("Designer Lookbook Product")
		verbose_name_plural = _("Designer Lookbook Products")

	def __unicode__(self):
		return unicode(self.deslookbook)
"""
