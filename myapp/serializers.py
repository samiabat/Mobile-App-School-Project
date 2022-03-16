from pyexpat import model
from turtle import mode
from rest_framework.serializers import ModelSerializer
from django.http import JsonResponse


from .models import User, App


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class AppSerializer(ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'