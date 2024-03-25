from django.urls import path
from payment_forms.forms.views import get_item, get_payment_session

app_name = 'forms'


urlpatterns = [
    path('item/', get_item, name='get_item'),
    path('buy/', get_payment_session, name='get_payment_session')
]