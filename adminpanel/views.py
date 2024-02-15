from django.shortcuts import render, redirect
from homepage.decorators import author_required
from homepage.models import Profile, Order, Cart, Product, Message
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required
from  django.contrib import messages

# Create your views here.
@author_required
def admin_header(request):
    return render(request, 'adminpanel/admin_header.html')

@login_required(login_url='/login/')
@author_required
def admin_page(request):
    total_pending = 0
    total_completed = 0

    select_pending = Order.objects.filter(payment_status = 'p')
    select_complete = Order.objects.filter(payment_status = 'completed')
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
    if complete_count > 0:
        for order in select_complete:
            total_price = order.total_price
            total_completed += total_price
            

    context = {
        'pending_count':pending_count,
        'complete_count':complete_count,
        'number_of_order':number_of_order,
        'number_of_product':number_of_product,
        'number_of_user':number_of_user,
        'number_of_admin':number_of_admin,
        'number_of_account':number_of_account,
        'number_of_message': number_of_message

    }

    return render(request, 'adminpanel/admin_page.html', context)

def admin_order(request):
    select_order = Order.objects.all()
    count_order = select_order.count()

    
    context = {
        'count_order': count_order,
        'select_order': select_order,
        
    }
            
    if request.method == 'POST':
        update_payment = request.POST['update_payment']
        update_order = request.POST['update_order']

        name = request.POST['name']
        if update_order:
            updateOrder = Order.objects.get(name = name)
            updateOrder.payment_status = update_payment
            updateOrder.save()
            messages.success(request, 'cart quantity updated!')
            return redirect ('/admin_order/')

    return render(request, 'adminpanel/admin_orders.html',context)


@author_required
def deleteorder(request, id):
    order_item = Order.objects.get(id = id)
    order_item.delete()
    return redirect('/admin_order/')




