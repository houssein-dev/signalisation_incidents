from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import incidents, getOne

schema_view = get_schema_view(
   openapi.Info(
      title="Incident API",
      default_version='v1',
      description="API pour gérer les incidents",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="houceinhmd@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('incidents/', incidents, name='incidents'),
    path('incidents/<int:pk>/', getOne, name='getOne'),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
]
