from rest_framework import serializers
from .models import MyUser


class RegistrationSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = MyUser
        fields = ('username', 'password', 'email')
        extra_fields = {
            'password': {'write_only': True},
        }

    def save(self):
            user = MyUser(
                email=self.validated_data['email'],
                username=self.validated_data['username']
            )
            password = self.validated_data['password']

            user.set_password(password)
            user.save()
            return user