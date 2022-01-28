from django.urls import path, include
from .views import *


urlpatterns = [
    path('', index),
    path('app/', app),
    path('gotcha/', gotcha),
    path('test_api/', ApiTest.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
]
