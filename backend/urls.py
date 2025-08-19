from django.contrib import admin
from django.urls import path, include
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/login", TokenObtainPairView.as_view(), name="get_token"),
    path("api/", include("api.urls")),
    path("mails/", include("mailservice.urls"))
]
