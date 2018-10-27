
from django.urls import path
from .views import CreateUserView,LoginView,LogoutView,CabAvailablelistView

app_name = 'bookings'

urlpatterns = [
    path('user/register', CreateUserView.as_view(),name = 'user-register'), 
    path('bookings/available',CabAvailablelistView.as_view(),name= 'cab-available'),
    path('user/login', LoginView.as_view(),name = 'user-login'),
    path('user/logout', LogoutView.as_view(),name = 'user-logout')
    
]