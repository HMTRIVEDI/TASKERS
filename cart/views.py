from django.shortcuts import render, redirect


def show_cart(request):

    return render(request, 'cart/cart.html')


def add_booking(request, tasker_id):

    date = request.POST.get('date')
    time = request.POST.get('time')
    hours = int(request.POST.get('hours'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if tasker_id in list(cart.keys()):
        cart[tasker_id] = date, time, hours
    else:
        cart[tasker_id] = date, time, hours

    request.session['cart'] = cart
    print(cart)
    return redirect(redirect_url)
