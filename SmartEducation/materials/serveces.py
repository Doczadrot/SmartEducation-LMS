
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_stripe_price(course):
    """Создаю цену и продукт по библиотeки страйп"""
    stripe_product = stripe.Product.create(name=course.title)
    stripe_price = stripe.Price.create(product=stripe_product.id,
                                       unit_amount=int(course.price * 100),currency="rub",)
    return stripe_price

def create_stripe_pay(price_id):
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",  #при успешной оплате
        cancel_url="http://127.0.0.1:8000/",  #при отмене оплаты
        line_items=[{ "price": price_id, "quantity": 1, }, ], mode="payment",)
    return session.url