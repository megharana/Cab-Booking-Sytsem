from django.contrib import admin
from .models import User,Driver,CarModel,CabRideStatus,PaymentOption,Cab

from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {
          'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }

admin.site.register(User)
admin.site.register(Driver)
admin.site.register(CarModel)

admin.site.register(CabRideStatus)
admin.site.register(PaymentOption)
admin.site.register(Cab)



