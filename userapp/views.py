from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import RegistrationSerializers


class Registration(APIView):

    def post(self, request):
        serializer = RegistrationSerializers(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['request'] = 'successfuly registered a new user'
            data['email'] = user.email
            data['username'] = user.username
        else:
            data = serializer.errors
        return Response(data)