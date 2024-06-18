from django.urls import path
from kashmir.views import *
app_name='kashmir'

urlpatterns = [
    path('kashmir/',kashmir,name='kashmir'),
]
