from django.urls import path
from . import views

urlpatterns = [
    path('userclient/',views.userclient),
    path('login/',views.login),
    path('signup/',views.signup),
    path('messages/',views.uploadjson),
    path('userclient/compose/',views.compose)
]