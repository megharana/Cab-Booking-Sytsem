from rest_framework import serializers,exceptions
from django.contrib.auth.hashers import make_password   #for hashing password in drf
#from django.contrib.auth import authenticate
from bookings.models import User,Cab

class UserRegistrationPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','pswd']


class CabListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cab
        fields = (
            'lisence', 
            'carModel_Id'
        ) 

   

    