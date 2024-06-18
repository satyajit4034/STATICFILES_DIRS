from django.urls import path
from bangalore.views import *
app_name='bangalore'

urlpatterns = [
    path('bangalore/',bangalore,name='bangalore'),
]
