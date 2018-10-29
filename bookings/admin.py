from django.contrib import admin
from .models import User,Driver,CarModel,CabRideStatus,PaymentOption,Cab


admin.site.register(User)
admin.site.register(Driver)
admin.site.register(CarModel)

admin.site.register(CabRideStatus)
admin.site.register(PaymentOption)
admin.site.register(Cab)



