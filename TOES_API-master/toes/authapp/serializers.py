from djoser.serializers import UserCreateSerializer, UserSerializer
from .models import *
from rest_framework import generics,serializers
from . models import (
    User,WorkerDetails,JobDetails, Categories,
    StatusMaster, RecruitersRequests, WorkersRequests , 
    )

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('is_superuser','is_admin','name','username','email','password',
                        'dob','gender','aadhar_no', 'profile_image','phone')

class WorkerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerDetails
        fields = '__all__'


class JobDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDetails
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
        

class StatusMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusMaster
        fields = '__all__'


class RecruitersRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitersRequests
        fields = '__all__'

class WorkersRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkersRequests
        fields = '__all__'
