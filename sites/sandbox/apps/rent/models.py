from django.utils.translation import ugettext_lazy as _
from datetime import datetime, date

from django.db import models
from datetime import datetime, timedelta

from apps.partner.models import StockRecord
from oscar.core.compat import AUTH_USER_MODEL


class Rent(models.Model):
    customer = models.ForeignKey(AUTH_USER_MODEL, verbose_name=_("Customer name"), null=True, blank=True, unique=True)

    stock_record = models.ForeignKey(StockRecord, verbose_name=_("Stock Record"), null=True, blank=True)

    CHOICES = (('4', '4'), ('8', '8'))
    period = models.IntegerField(_('Rent Period'), max_length=30, choices=CHOICES, null=True)

    start_date = models.DateTimeField(_('Rent start date'), auto_now_add=True)
    end_date = models.DateTimeField(_('Rent end date'), auto_now_add=True)


    def save(self, *args, **kwargs):
        d = timedelta(days=self.period)
        super(Rent, self).save(*args, **kwargs)
        ##To get the start_date
        self.end_date = self.start_date + d
        super(Rent, self).save(*args, **kwargs)


    def __unicode__(self):
        return unicode(self.product)
