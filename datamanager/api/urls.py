from django.urls import path

from api.views import Fruit, Provider

urlpatterns = [
    path('fruit/', Fruit.fruit),
    path('provider/', Provider.provider)
]
