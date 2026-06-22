
from rest_framework import serializers
from .models import User,Quote

class Inputdata(serializers.Serializer):
    count = serializers.IntegerField()

class Outputdata(serializers.Serializer):
    text = serializers.CharField(max_length=50)

class UserRegistration(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20)
