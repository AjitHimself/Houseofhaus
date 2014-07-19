from django.utils.translation import ugettext_lazy as _

from django.db import models
# from filters.models import FilterType, ProductFilter
from designer.models import Designer
from oscar.core.loading import get_classes, get_model
from oscar.apps.catalogue.abstract_models import AbstractProduct, AbstractCategory



# FilterType = get_model('filters','FilterType')
# ProductFilter = get_model('filters','ProductFilter')

class Product(AbstractProduct):
    designer = models.ForeignKey(Designer, verbose_name=_("Designer"), null=True, blank=True, related_name='products')

    #video =models.FileField(upload_to='Product_videos',blank=True,null=True)

    filter = models.ManyToManyField('FilterType', through='ProductFilter', blank=True)

    filter_options = models.ManyToManyField('FilterOption', verbose_name=_("Filter Options"), null=True, blank=True,
                                            related_name='filter_options', )

class Category(AbstractCategory):
    pass

class DesLookbook(models.Model):
    designer = models.ForeignKey(Designer, verbose_name=_("Designer"), null=True, blank=True, related_name='lookbooks')

    name = models.CharField(_("Lookbook name"), max_length=128, null=True, unique=True)

    products = models.ManyToManyField(Product, verbose_name=_("Product"), related_name='lookbooks', null=True,
                                      blank=True)

    description = models.TextField(_("Message"))

    slug = models.SlugField(_('Slug'), max_length=255, editable=True, null=True)

    class Meta:
        verbose_name = _("Designer Lookbook")
        verbose_name_plural = _("Designer Lookbooks")

    def get_absolute_url(self):
        designer_slug = self.designer.slug
        return reverse('designer:lookbook',
                       kwargs={'designer_slug': designer_slug, 'lookbook_slug': self.slug, 'pk': self.id, })

    def __unicode__(self):
        return unicode(self.name)

class FilterType(models.Model):
    category = models.ForeignKey(Category, related_name='category_filters')
    name = models.CharField(_('Name'), max_length=30, null=True)

    class Meta:
        unique_together = ("category", "name")
        verbose_name = _("Filter Type")
        verbose_name_plural = _("Filter Types")

    def __unicode__(self):
        return unicode(self.name)


class FilterOption(models.Model):
    filters = models.ForeignKey('FilterType', verbose_name=_("Filter Type"), related_name='options')
    name = models.CharField(_('Options'), max_length=30, null=True)

    class Meta:
        #unique_together = ("category", "name")
        verbose_name = _("Filter Option")
        verbose_name_plural = _("Filter Options")

    def __unicode__(self):
        option_description = '%s: %s' % (self.filters, self.name)
        return unicode(option_description)


class ProductFilter(models.Model):
    filters = models.ForeignKey('FilterType', )
    product = models.ForeignKey(Product, related_name='product_filters')
    option = models.ForeignKey('FilterOption', )

    class Meta:
        unique_together = ("filters", "product")
        verbose_name = _("Product Filter")
        verbose_name_plural = _("Product Filters")


from oscar.apps.catalogue.models import *


