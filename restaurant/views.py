from django.shortcuts import render, redirect
import random
import datetime

# Create your views here.
menu_items = {
    'Sushi': 10.99,
    'Pizza': 5.99,
    'Burger': 6.99,
    'Coffee': 2.99,
    'Pretzel': 4.99,
}

def main(request):
    return render(request, 'restaurant/main.html')

def order(request):
    daily_special = random.choice(list(menu_items.keys()))

    if request.method == 'POST':
        return redirect('confirmation')

    context = {
        'daily_special': daily_special,
        'menu_items': menu_items,
    }
    return render(request, 'restaurant/order.html', context)

def confirmation(request):
    if request.method == "POST":
        ordered_items = {item: menu_items[item] for item in request.POST if item in menu_items}
        special_instructions = request.POST.get('instructions', '')
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')

        total_price = sum(ordered_items.values())
        ready_time = datetime.datetime.now() + datetime.timedelta(minutes=random.randint(30, 60))

        context = {
            'ordered_items': ordered_items,
            'total_price': total_price,
            'special_instructions': special_instructions,
            'name': name,
            'phone': phone,
            'email': email,
            'ready_time': ready_time.strftime("%Y-%m-%d %H:%M"),
        }
        return render(request, 'restaurant/confirmation.html', context)
    else:
        return render(request, 'restaurant/order.html')
    
def landing_page(request):
    return render(request, 'restaurant/main.html')