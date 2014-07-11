import django.dispatch

basket_addition = django.dispatch.Signal(
    providing_args=["product", "user", "request"])
# @ajit : New Signal added to notify a rent is added
# to basket
basket_rent_addition = django.dispatch.Signal(
	providing_args=["product","user","request"])
voucher_addition = django.dispatch.Signal(
    providing_args=["basket", "voucher"])
voucher_removal = django.dispatch.Signal(
    providing_args=["basket", "voucher"])
