from django.utils.translation import ugettext_lazy as _

from django.db import models

from oscar.apps.order.abstract_models import AbstractOrder

class Order(AbstractOrder):
	on_rent=models.BooleanField(_("Is product on rent?"),default=True)


from oscar.apps.order.models import *  # noqa


