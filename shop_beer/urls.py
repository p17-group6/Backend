from django.contrib import admin
from django.urls import path, re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi  

from rest_framework import permissions
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from auth_beer import views

schema_view = get_schema_view(
   openapi.Info(
      title="Auth Beer API",
      default_version='v1',
      description="Auth Microservice Django API",
      terms_of_service="https://www.google.com/policies/terms/",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path('^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path('^redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/',         admin.site.urls),
    path('login/',         TokenObtainPairView.as_view()),
    path('refresh/',       TokenRefreshView.as_view()),
    path('verifyToken/',   views.VerifyTokenView.as_view()),
    path('user/',          views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('user/<int:pk>/update/', views.UserUpdateView().as_view()),
    path('user/<int:pk>/delete/', views.UserDeleteView.as_view())
]
