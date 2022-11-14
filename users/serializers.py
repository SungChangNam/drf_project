from rest_framework.views import APIView
from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from articles.serializers import ArticleListSerializer




class UserProfileSerializer(serializers.ModelSerializer):
    followers = serializers.StringRelatedField(many=True, read_only=True)
    followings = serializers.StringRelatedField(many=True, read_only=True)
    article_set =ArticleListSerializer(many=True)
    like_articles = ArticleListSerializer(many=True)
    class Meta:
        model = User
        fields=("id","email","followings","followers","article_set", "like_articles")



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
