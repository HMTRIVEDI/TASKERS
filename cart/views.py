from django.shortcuts import render, redirect, reverse


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
    return redirect(redirect_url)


def delete_booking(request, item_id):

    cart = request.session.get('cart', {})
    if item_id in cart:
        cart.pop(item_id)
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    print(cart)
    return redirect(reverse('show_cart'))


def update_booking(request, item_id):

    date = request.POST.get('date')
    time = request.POST.get('time')
    hours = int(request.POST.get('hours'))
    cart = request.session.get('cart', {})

    if hours > 8:
        print(" no more then 8 hours ")
    elif hours > 0 and hours < 9:
        if item_id in list(cart.keys()):
            cart[item_id] = date, time, hours
        else:
            cart[item_id] = date, time, hours
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    print(cart)
    return redirect(reverse('show_cart'))
