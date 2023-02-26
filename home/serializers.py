from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# class UnitSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Unit
#         fields = '__all__'

# class RequirementsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Requirements
#         fields = '__all__'

# class SiteVisitSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SiteVisit
#         fields = '__all__'

class FlatSerializer(serializers.ModelSerializer):
    class Meta:
            model = Flat
            fields = '__all__'

class FlatmateSerializer(serializers.ModelSerializer):
    class Meta:
            model = Flatmate
            fields = '__all__'