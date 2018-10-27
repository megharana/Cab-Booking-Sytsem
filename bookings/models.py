from django.db import models
from django_google_maps import fields as map_fields

class Rental(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)

    
class User(models.Model):
    user_Id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    pswd = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)

class Driver(models.Model):
    driver_Id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    pswd = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    driving_lisence = models.CharField(max_length=15)

class CarModel(models.Model):
    carModel_Id = models.AutoField(primary_key=True)
    modelName = models.CharField(max_length = 15)

class Cab(models.Model):
    cab_Id = models.AutoField(primary_key=True)
    lisence = models.CharField(max_length=15)
    carModel_Id = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    driver_Id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)   # false = Available and true = taken



# class CabRide_User(models.Model):
#     cabRideUser_Id = models.AutoField(primary_key=True)
#     userRide_Source = 
#     userRide_Dest
#     ride_startTime = 
#     ride_endTime
#     payment_Id
#     fare 
#     cabRideStatus_Id
#     cab_Id
#     driver_Id
#     user_Id = 

    

# class DriverRide_User(models.Model):
#     driverRide_Id = models.AutoField(primary_key=True)
#     driverRide_Source 
#     driverRide_Dest
#     ride_startTime = 
#     ride_endTime
#     payment_Id
#     fare 
#     cab_Id
#     driver_Id
#     user_Id = 

class CabRideStatus(models.Model):
    cabRideStatus_Id = models.BooleanField(primary_key=True)
    cabRideStatus_Name = models.CharField(max_length=15)

class PaymentOption(models.Model):
    paymentOption_Id = models.AutoField(primary_key=True)
    paymentOption_Name = models.CharField(max_length = 30)



