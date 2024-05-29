from django.urls import path
from .views import *


app_name ='main'

urlpatterns = [
    path('',index,name='index'),
    path('daraja/stk-push/',stk_push,name='stk_push')
]
