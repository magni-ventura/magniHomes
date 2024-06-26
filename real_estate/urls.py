"""
URL configuration for real_estate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('magnihomes/', admin.site.urls),

    path("api/v1/auth/", include("djoser.urls")),

    path("api/v1/auth/", include("djoser.urls.jwt")),

    path("api/v1/profile/", include("apps.profiles.urls")),

    path("api/v1/properties/", include("apps.properties.urls")),

    path("api/v1/ratings/", include("apps.ratings.urls")),

    path("api/v1/enquiries/", include("apps.enquiries.urls")),

]

admin.site.site_header = "Magni Homes Admin",
admin.site.site_title = "Magni Homes Portal",
admin.site.index_title = "Welcome to The Magni Homes Portal",