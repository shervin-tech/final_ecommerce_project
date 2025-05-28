from django import template
from shopping_cart.models import CartItem

register = template.Library()

@register.filter
def cart_items_count(user):
    if user.is_authenticated:
        return CartItem.objects.filter(user=user).count()
    return 0 