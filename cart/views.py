from django.shortcuts import render, redirect


def show_cart(request):

    return render(request, 'cart/cart.html')


def add_booking(request, tasker_id):

    date = request.POST.get('date')
    time = request.POST.get('time')
    hours = int(request.POST.get('hours'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    
    print(request.POST.get('date'))
    print(request.POST.get('time'))
    print(request.POST.get('hours'))
    print(request.POST.get('redirect_url'))
    

    if tasker_id in list(cart.keys()):
        cart[tasker_id] = date, time, hours
        
    request.session['cart'] = cart
    print(request.session.get('cart', {}))
    return redirect(redirect_url)
