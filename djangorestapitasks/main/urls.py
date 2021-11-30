from django.urls import path, include
from . import views
from .views import *
from .views import ProductViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Products',ProductViewset)


urlpatterns =[
    path('api/', include(router.urls))
]