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

    if int(hours) in range(1, 8):
        if item_id in list(cart.keys()):
            cart[item_id] = date, time, hours
        else:
            cart[item_id] = date, time, hours
    elif hours > 8:
        print('must be less then 8')
    else:
        cart.pop(item_id)

    request.session['cart'] = cart
    print(cart)
    return redirect(reverse('show_cart'))
