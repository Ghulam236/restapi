
from django.contrib import admin
from django.urls import path
from drfapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("studentapi/",views.StudentList.as_view()),
    # path("studentapi/",views.StudentCreate.as_view()),

    # path("studentapi/",views.LCStudentList.as_view()),


    # path("studentapi/<int:pk>/",views.StudentRetrieve.as_view())
    # path("studentapi/<int:pk>/",views.StudentUpdate.as_view())
    # path("studentapi/<int:pk>/",views.StudentDestroy.as_view())
    path("studentapi/",views.LCStudentList.as_view()),
    path("studentapi/<int:pk>/",views.RUDLCStudentList.as_view())




]
