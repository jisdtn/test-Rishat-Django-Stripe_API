import os

from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe

from .models import Item
from django.conf import settings
# from dotenv import load_dotenv

# load_dotenv()

#= os.getenv('stripe.api_key')
stripe.api_key = 'sk_test_51Oy8pMJ1o8g4ent6gJJbKYakIS2JitAp1qDpBJW9R5dMk4XvuUxW2HHhOXCf4tIXXPUrUrFGxo3gx3aXHQfV7Tuu009TnA8exR'

def success_view(request):
    return render(request, 'success.html')
@csrf_exempt
def create_checkout_session(request, item_id):
    """Creation of payment session with API Stripe"""
    item = Item.objects.get(id=item_id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url = 'http://localhost:8000/success'
    )
    return JsonResponse({'session_id': session.id})


def item_detail(request, item_id):
    """Get the item detail"""
    item = Item.objects.get(id=item_id)
    return render(request, 'item_detail.html', {'item': item, 'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY})

