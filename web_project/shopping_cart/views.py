from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from store.models import Product
from .models import CartItem
from .forms import CartAddProductForm, CheckoutForm
from users.models import Order, OrderItem

# Create your views here.

@login_required
def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.get_total_price() for item in cart_items)
    return render(request, 'shopping_cart/cart_detail.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def add_to_cart(request, product_id):
    if request.method == 'POST':
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            product = get_object_or_404(Product, id=product_id)
            quantity = form.cleaned_data['quantity']
            cart_item, created = CartItem.objects.get_or_create(
                user=request.user,
                product=product,
                defaults={'quantity': quantity}
            )
            if not created:
                cart_item.quantity += quantity
                cart_item.save()
            messages.success(request, f'{product.name} added to cart.')
            return redirect('shopping_cart:cart_detail')
    return redirect('store:product_list')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()
    messages.success(request, f'{cart_item.product.name} removed from cart.')
    return redirect('shopping_cart:cart_detail')

@login_required
def update_quantity(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    try:
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    except ValueError:
        messages.error(request, 'Invalid quantity.')
    return redirect('shopping_cart:cart_detail')

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    if not cart_items.exists():
        messages.error(request, 'Your cart is empty.')
        return redirect('shopping_cart:cart_detail')

    if request.method == 'POST':
        form = CheckoutForm(request.user, request.POST)
        if form.is_valid():
            shipping_address = form.cleaned_data['shipping_address']
            total_amount = sum(item.get_total_price() for item in cart_items)

            # Create the order
            order = Order.objects.create(
                user=request.user,
                shipping_address=shipping_address,
                total_amount=total_amount
            )

            # Create order items from cart items
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price
                )

            # Clear the cart
            cart_items.delete()

            messages.success(request, 'Order placed successfully!')
            return redirect('users:order_detail', pk=order.id)
    else:
        form = CheckoutForm(request.user)

    return render(request, 'shopping_cart/checkout.html', {
        'form': form,
        'cart_items': cart_items,
        'total': sum(item.get_total_price() for item in cart_items)
    })
