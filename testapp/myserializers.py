from rest_framework import serializers
from . import models

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.UserInfo
        fields = '__all__'

class InspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = models.InspectionInfo
        fields = '__all__'
