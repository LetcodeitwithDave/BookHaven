from django.shortcuts import render
from homepage.decorators import author_required
from homepage.models import Profile, Order, Cart, Product, Message
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required

# Create your views here.
@author_required
def admin_header(request):
    return render(request, 'adminpanel/admin_header.html')

@login_required(login_url='/login/')
@author_required
def admin_page(request):
    total_pending = 0
    total_completed = 0

    select_pending = Order.objects.filter(payment_status = 'pending')
    select_complete = Order.objects.filter(payment_status = 'complete')
    select_order  = Order.objects.filter()
    select_product = Product.objects.filter()
    select_user =  Group.objects.get(name='User')
    select_admin = Group.objects.get(name= 'Author')
    select_account = Profile.objects.filter()
    select_message = Message.objects.filter()

    pending_count = select_pending.count()
    complete_count = select_complete.count() 
    number_of_order = select_order.count()
    number_of_product = select_product.count()
    number_of_user = select_user.user_set.count()
    number_of_admin = select_admin.user_set.count()
    number_of_account = select_account.count()
    number_of_message = select_message.count()

    if pending_count > 0:
        for order in select_pending:
            total_price = order.total_price
            total_pending += total_price

    elif complete_count > 0:
        for order in select_complete:
            total_price = order.total_price
            total_completed += total_price


    context = {
        'total_pending':total_pending,
        'total_completed':total_completed,
        'number_of_order':number_of_order,
        'number_of_product':number_of_product,
        'number_of_user':number_of_user,
        'number_of_admin':number_of_admin,
        'number_of_account':number_of_account,
        'number_of_message': number_of_message

    }

    return render(request, 'adminpanel/admin_page.html', context)