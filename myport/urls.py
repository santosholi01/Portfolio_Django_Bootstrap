from django.urls import path
from .views import home,contractuser


urlpatterns = [
    path('',contractuser.as_view(), name="home" )

]
