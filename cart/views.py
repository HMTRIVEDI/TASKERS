from django.shortcuts import render, redirect


def show_cart(request):

    return render(request, 'cart/cart.html')

def add_booking(request, tasker_id):

    date = request.POST.get('date')
    time = request.POST.get('time')
    propertysize = int(request.POST.get('propertysize'))
    hours = int(request.POST.get('hours'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart',{})
    
    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
    