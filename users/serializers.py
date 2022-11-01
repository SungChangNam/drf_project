from rest_framework.views import APIView
from rest_framework import serializers
import users
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        
        model = User
        fields = "__all__"
        
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        pass
        return user
    
    def update(self,validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        pass
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)


        token['email'] = user.email


        return token
