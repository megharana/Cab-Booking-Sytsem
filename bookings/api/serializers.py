from rest_framework import serializers,exceptions
from django.contrib.auth.hashers import make_password   #for hashing password in drf
#from django.contrib.auth import authenticate
from bookings.models import User,Cab

class UserRegistrationPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    
class LoginSerializer(serializers.Serializer):
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

   

    # def validate(self, data):
    #     email = data.get("email", "")
    #     pswd = data.get("pswd","")

    #     if email and pswd :
    #         user = authenticate(email = email, pswd = pswd)
    #         print(user)
    #         if user:
    #             if user.is_active:
    #                 data['user'] = user
    #             else:
    #                 msg = "User is inactive"
    #                 raise exceptions.ValidationError(msg)
    #         else:
    #             msg = "Unable to login with above credentials"
    #             raise exceptions.ValidationError(msg)
    #     else:
    #         msg = "Please provide credentials"
    #         raise exceptions.ValidationError(msg)
    #     return user