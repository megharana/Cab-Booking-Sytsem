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
    model = get_user_model()
    permission = (AllowAny)
    serializer_class = UserRegistrationPostSerializer


class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data = request.data)
                  
        user= User.objects.all()
        querySet_length = len(user)
        try:
            for i in range(querySet_length):
            
                if(len(request.data['email'])>0 and len(request.data['pswd'])>0):
            

                    if(request.data['email'] == user[i].email and request.data['pswd'] == user[i].pswd):
                        print("Authenticated")
                        userLoggedIn = user[i].email
                        
                        return HttpResponseRedirect("/cab/user/set/locations/")
                        break
                
                    
                else:
                    msg = "Must provide credentials"
                    raise exceptions.ValidationError(msg)
                    
                    break

            msg = "Credentials wrong"
            raise exceptions.ValidationError(msg) 
        
        except MultiValueDictKeyError as e:
            return Response(e.args[0]) 
        # serializer.is_valid(raise_exception = True)
        # user = serializer.validated_data['user']
        # django_login(request, user)
        # token, created = Token.objects.get_or_create(user = user)
        return Response(request.data, status = 200)

    
class CabAvailablelistView(generics.ListAPIView):
    serializer_class = CabListSerializer
    permission_class = [permissions.IsAuthenticated]
    # queryset = Cab.objects.all()
    def get_queryset(self):
        cab_available = Cab.objects.filter(status = False)
        
        return cab_available
        #return Response(cab_available,status = 200)

def mapview(request):
    # return HttpResponse("<h1>This is after login page</h1>")
    return render(request,'mapview.html')

def setDistanceDuration(request):
    
    if request.method == 'POST' and 'mapInfo' in request.POST:
        mapInfoForm = mapInfo_Form(request.POST) 
        
        global mapInfo
        if mapInfoForm.is_valid():
            mapInfo = mapInfoForm.cleaned_data['mapInfo'].split(",")
            
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
    authentication_classes = (TokenAuthentication)

    def post(self,request):
        django_logout(request)
        return Response(status = 204)

