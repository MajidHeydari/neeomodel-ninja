from django.conf.urls import url
from .views import connectPaP,connectPaC,cityDetails,personDetails,getAllPersons,getAllCities
from django.urls import path
from .api import api

urlpatterns = [
    path('person',personDetails),
    path('getAllPersons',getAllPersons),
    path('city',cityDetails),
    path('getAllCities',getAllCities),
    path('connectPaC',connectPaC),
    path('connectPaP',connectPaP),
    path("api/", api.urls),
]