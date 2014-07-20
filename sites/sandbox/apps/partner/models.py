from django.utils.translation import ugettext_lazy as _

from django.db import models

from oscar.apps.partner.abstract_models import AbstractStockRecord, AbstractPartner

from oscar.core.compat import AUTH_USER_MODEL


class StockRecord(AbstractStockRecord):
    rent_cost = models.DecimalField(_("Rent Cost"), decimal_places=2, max_digits=12, blank=True, null=True)

    rent_count = models.IntegerField(_("Rent Count"), null=True, default=0)

class Partner(AbstractPartner):
    designer = models.ForeignKey(AUTH_USER_MODEL, limit_choices_to={'is_designer': True},
                                 verbose_name=_("Partner name"), null=True, blank=True, unique=True)
    users = models.ManyToManyField(AUTH_USER_MODEL, related_name="partners",
                                   blank=True, null=True, verbose_name=_("Users"))

    description = models.TextField(null=True)


from oscar.apps.partner.models import *  # noqa


