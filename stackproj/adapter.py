from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site


class MyConfirmAdapter(DefaultAccountAdapter):

    def get_email_confirmation_url(self, request, emailconfirmation):
        url = "{protocol}://{domain}/accounts-rest/registration/account-confirm-email/{email_key}".format(
            protocol=request.scheme,
            domain=request.get_host(),
            email_key=emailconfirmation.key)
        ret = request.build_absolute_uri(url)
        return ret
