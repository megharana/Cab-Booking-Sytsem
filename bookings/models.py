from django.db import models
from django_google_maps import fields as map_fields


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

class CabRideStatus(models.Model):
    cabRideStatus_Id = models.BooleanField(primary_key=True)
    cabRideStatus_Name = models.CharField(max_length=15)

class PaymentOption(models.Model):
    paymentOption_Id = models.AutoField(primary_key=True)
    paymentOption_Name = models.CharField(max_length = 30)

class CabRide_User(models.Model):
    cabRideUser_Id = models.AutoField(primary_key=True)
    userRide_Source = models.CharField(max_length=40)
    userRide_Dest =  models.CharField(max_length=40)
    ride_startTime = models.DateTimeField(auto_now_add=True)
    ride_endTime = models.DateTimeField(auto_now_add=True)
    payment_Id = models.ForeignKey(PaymentOption, on_delete=models.CASCADE)
    fare = models.DecimalField(max_digits=10, decimal_places=2)
    cabRideStatus_Id = models.ForeignKey(CabRideStatus, on_delete=models.CASCADE)
    cab_Id = models.ForeignKey(Cab, on_delete=models.CASCADE)
    driver_Id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    user_Id = models.ForeignKey(User, on_delete=models.CASCADE)

class DriverRide_User(models.Model):
    driverRide_Id = models.AutoField(primary_key=True)
    driverRide_Source = models.CharField(max_length=40)
    driverRide_Dest =  models.CharField(max_length=40)
    ride_startTime = models.DateTimeField(auto_now_add=True)
    ride_endTime = models.DateTimeField(auto_now_add=True)
    payment_Id = models.ForeignKey(PaymentOption, on_delete=models.CASCADE)
    fare = models.DecimalField(max_digits=10, decimal_places=2)
    cab_Id = models.ForeignKey(Cab, on_delete=models.CASCADE)
    driver_Id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    user_Id = models.ForeignKey(User, on_delete=models.CASCADE)    





