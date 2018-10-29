from bookings.models import User,Cab,CabRide_User
from django.shortcuts import render
from rest_framework import generics,exceptions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics,permissions
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationPostSerializer,LoginSerializer,CabListSerializer
from django.contrib.auth import get_user_model, login as django_login, logout as django_logout
from rest_framework.authtoken.models import Token

from .forms import mapInfo_Form
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponseRedirect,HttpResponse

class CreateUserView(generics.CreateAPIView):
    """
    Views that will allow for user registeration  
    """
    permission = (AllowAny)
    serializer_class = UserRegistrationPostSerializer


class LoginView(APIView):
    """
    Authenticating the registered user
    """
    def post(self,request):
        serializer = LoginSerializer(data = request.data)
                  
        user= User.objects.all()
        querySet_length = len(user)
        try:
            for i in range(querySet_length):
            
                if(len(request.data['email'])>0 and len(request.data['pswd'])>0):  #checking if data is passed in JSON form 
            

                    if(request.data['email'] == user[i].email and request.data['pswd'] == user[i].pswd):    #verifying the registered details with the passed JSON data
                        print("Authenticated")
                        userLoggedIn = user[i].email
                        
                        return HttpResponseRedirect("/cab/user/set/locations/")   #redirecting to mapview.html page
                        break
                
                    
                else:
                    msg = "Must provide credentials"      
                    raise exceptions.ValidationError(msg)   
                    
                    break

            msg = "Credentials wrong"
            raise exceptions.ValidationError(msg) 
        
        except MultiValueDictKeyError as e:
            return Response(e.args[0]) 
        
        return Response(request.data, status = 200)

    
class CabAvailablelistView(generics.ListAPIView):
    """
    Available Cabs will be displayed based on status field (false = Available and true = taken)
    """
    serializer_class = CabListSerializer
    permission_class = [permissions.IsAuthenticated]
    # queryset = Cab.objects.all()
    def get_queryset(self):
        cab_available = Cab.objects.filter(status = False)
        
        return cab_available
        #return Response(cab_available,status = 200)

def mapview(request):
    """
    rendering mapview.html template 
    """
    return render(request,'mapview.html')

def setDistanceDuration(request):
    """
    function for fetching source and destination of Ride and fetching duration and distance of resultant route.
    """
    if request.method == 'POST' and 'mapInfo' in request.POST:
        mapInfoForm = mapInfo_Form(request.POST) 
        
        global mapInfo
        if mapInfoForm.is_valid():
            mapInfo = mapInfoForm.cleaned_data['mapInfo'].split("/")
            
            #u_Id = User.objects.filter(email=userLoggedIn)[0].user_Id
            # u_Id_CabRide = CabRide_User.objects.get(user_Id=u_Id)
            # u_Id_CabRide.userRide_Source = mapInfo[0]
            # u_Id_CabRide.userRide_Dest = mapInfo[1]
            # u_Id_CabRide.save()
            print("The Source of Ride",mapInfo[0])
            print("The destination of Ride",mapInfo[1])
        else:
            
		#Handling the get request  
            mapInfoForm = mapInfo_Form()
    return HttpResponseRedirect("/cab/bookings/available")

class LogoutView(APIView):
    """
    for Logout 
    """
    pass

