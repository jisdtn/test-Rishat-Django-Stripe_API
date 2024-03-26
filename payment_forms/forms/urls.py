from django.urls import path

from .views import create_checkout_session, item_detail, success_view

app_name = 'forms'


urlpatterns = [
    path('item/<int:item_id>/', item_detail, name='item_detail'),
    path(
        'buy/<int:item_id>/',
        create_checkout_session,
        name='create_checkout_session'),
    path('success/', success_view, name='success')
]
