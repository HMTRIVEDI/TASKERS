from django.shortcuts import render, redirect


def show_cart(request):

    return render(request, 'cart/cart.html')


def add_booking(request, item_id):

    date = request.POST.get('date')
    time = request.POST.get('time')
    hours = int(request.POST.get('hours'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] = date, time, hours
    else:
        cart[item_id] = date, time, hours

    request.session['cart'] = cart
    print(cart)
    return redirect(redirect_url)
