from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from datetime import datetime, date

from django.db import models
from oscar.core.compat import AUTH_USER_MODEL
from oscar.core.loading import get_classes, get_model

from catalogue.models import Product, Category


class FilterType(models.Model):

	category = models.ForeignKey(Category,related_name='filters')
	name = models.CharField(_('Name'), max_length=30,editable= False, null=True)

	class Meta:
		#unique_together = ("category", "name")
		verbose_name = _("Filter Type")
		verbose_name_plural = _("Filter Types")

	def __unicode__(self):
		return unicode(self.name)


class FilterOption(models.Model):
	filters = models.ForeignKey('FilterType',related_name='options')
	name = models.CharField(_('Name'), max_length=30,editable= False, null=True)

	class Meta:
		#unique_together = ("category", "name")
		verbose_name = _("Filter Option")
		verbose_name_plural = _("Filter Options")

	def __unicode__(self):
		return unicode(self.name)



class ProductFilter(models.Model):

	filters = models.ForeignKey('FilterType',)
	product = models.ForeignKey(Product, related_name='filters')
	option = models.ForeignKey('FilterOption',)

	class Meta:
		unique_together = ("filters", "product")
		verbose_name = _("Product Filter")
		verbose_name_plural = _("Product Filters")

	# def __unicode__(self):
 #        return self.summary()

 #    def summary(self):
 #        return u"%s: %s" % (self.filters.name, self.value_as_text)

    # @property
    # def value_as_text(self):
    #     """
    #     Returns a string representation of the filter's value. To customise
    #     e.g. image attribute values, declare a _image_as_text property and
    #     return something appropriate.
    #     """
    #     property_name = '_%s_as_text' % self.filters.type
    #     return getattr(self, property_name, self.value)
