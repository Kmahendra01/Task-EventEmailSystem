from rest_framework import viewsets
from django.http import HttpResponse
from .models import EventType, Employee, Event
from .serializers import EventTypeSerializer, EmployeeSerializer, EventSerializer

def index(request):
    return HttpResponse("Welcome Event Email System")

class EventTypeViewSet(viewsets.ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer




