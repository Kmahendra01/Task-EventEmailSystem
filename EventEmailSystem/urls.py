
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('email_system.urls')),
    path('email_system/', include('email_system.urls')),
]



