from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.linkedin_oauth2.views import LinkedInOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from allauth.utils import build_absolute_uri


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class CustomOAuth2Adapter(LinkedInOAuth2Adapter):
   def get_callback_url(self, request, app):
        url = "{protocol}://{domain}/user/linkedin/login/callback/".format(
                protocol=request.scheme,
                domain=request.get_host()
                )
        ret = request.build_absolute_uri(url)
        print(ret)
        return ret