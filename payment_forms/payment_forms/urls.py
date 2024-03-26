from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('payment_forms.forms.urls', namespace='forms')),
]
