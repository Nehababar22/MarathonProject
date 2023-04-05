from rest_framework import routers
from Marathon_App import views

router = routers.DefaultRouter()

router.register(r'User', views.UserViewSet,basename='user')

