
from django.contrib import admin
from django.urls import path
from drfapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("studentapi/",views.hello_world),

    path("studentapi/<int:pk>/",views.hello_world)
]
