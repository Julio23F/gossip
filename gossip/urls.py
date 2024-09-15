from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("home/", include("pub.urls")),
    path('admin/', admin.site.urls),
    path("add/", include("add.urls")),
    path("auth/", include("accounts.urls")),
]
