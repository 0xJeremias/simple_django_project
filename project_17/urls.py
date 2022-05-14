"""project_17 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from project_17.views import (
    calculate_birth_year,
    hello_world,
    second_view,
    to_day,
    my_name,
    calculate_age,
    test_template,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello_world/", hello_world),
    path("second_view/", second_view),
    path("today/", to_day),
    path("my_name/<name>/<age>", my_name),
    path("calc_birth/<age>", calculate_birth_year),
    path("calculate_age/<str:birth_day>", calculate_age),
    path("test_template/", test_template),
]
