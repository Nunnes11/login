from django.urls import path
from . views import LoginPersonalizado

urlpatterns = [
    path('login/', LoginPersonalizado.as_view(), name='login'),
]