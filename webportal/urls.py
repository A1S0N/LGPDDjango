from django.urls import path
from .views import *

urlpatterns = [
    path('people', people_),
    path('models', models_),
    path('requests', lgpdreqs),
    path('requests/new', newLGPDReq),
]
