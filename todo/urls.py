from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from tarefa.api.viewsets import TasksViewSet
from user.api.viewsets import ProfilesViewSet

routes = routers.DefaultRouter()

routes.register('tasks', TasksViewSet, basename='Task')
routes.register('users', ProfilesViewSet, basename='Profile')

urlpatterns = [
    path('', include(routes.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
]
