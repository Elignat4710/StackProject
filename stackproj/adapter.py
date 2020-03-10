from allauth.account.adapter import DefaultAccountAdapter


class MyConfirmAdapter(DefaultAccountAdapter):

    def get_email_confirmation_redirect_url(self, request):
        path = 'http://localhost:8080/#/confirm_email'
        return path
