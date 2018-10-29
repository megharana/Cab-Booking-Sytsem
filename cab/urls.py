
from django.contrib import admin
from django.urls import path,include
from bookings.api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cab/',include('bookings.api.urls',namespace = 'api-bookings')),
    path('cab/user/set/locations/', views.mapview, name = 'api-mapview'),
    path('cab/user/info',views.setDistanceDuration, name = 'spi-userMapInfo')
]
