from django.urls import path
from bbsr.views import *
app_name='bbsr'

urlpatterns = [
    path('bbsr/',bbsr,name='bbsr'),
]
