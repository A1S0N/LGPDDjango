from django.urls import path
from .views import *

urlpatterns = [
#############  PRIVACYRLS ##########################
    path('rules', rules),
    path('rules/new', newRule),
    path('rules/edit', editRule),
    path('rules/delete', deleteRule),
#############   LGPDRQST  ##########################
    path('contact', contact, name='contact'),
]
