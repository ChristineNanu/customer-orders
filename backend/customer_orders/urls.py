"""
URL configuration for customer_orders project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

api_schema_view = get_schema_view(
    openapi.Info(
        title="Customer Orders API",
        default_version="v1",
        description="A simple API to manage customers and orders.",
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("mozilla_django_oidc.urls")),
    path(
        "api/",
        include(
            [
                path("", api_schema_view.with_ui("swagger", cache_timeout=0)),
                path("customers/", include("customers.urls")),
                path("orders/", include("orders.urls")),
            ]
        ),
    ),
]
