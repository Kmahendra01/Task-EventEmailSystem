from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventTypeViewSet, EmployeeViewSet, EventViewSet
from . import views

router = DefaultRouter()
router.register(r'event-types', EventTypeViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('', include(router.urls)),
]
print('hi')
