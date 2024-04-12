
from django.contrib import admin
from viewset import views
from rest_framework.routers import DefaultRouter
from django.urls import path,include

#  creating router object
router=DefaultRouter()
# register studentviewsert with router
router.register('studentapi',views.StudenViewtList,basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
