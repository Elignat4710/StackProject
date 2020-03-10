from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings


class MyConfirmAdapter(DefaultAccountAdapter):

    def send_mail(self, template_prefix, email, context):
        context['activate_url'] = settings.URL_BACK + \
            '/accounts-rest/registration/account-confirm-email/' + context['key']
        msg = self.render_mail(template_prefix, email, context)
        msg.send()
