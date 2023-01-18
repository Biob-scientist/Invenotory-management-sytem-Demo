from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product,Order
from .forms import ProductForm, OrderForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
@login_required
def product_delete(request,pk):
    item=Product.objects.get(id=pk)
    if request.method=='POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request,"dasboard/product_delete.html")


@login_required
def product_update(request,pk):
    item=Product.objects.get(id=pk)
    if request.method=='POST':
        form=ProductForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form=ProductForm(instance=item)
    context={
        'form':form,
    }
    return render(request,'dasboard/product_update.html', context)


@login_required
def index(request):
    orders=Order.objects.all()
    staff_count=User.objects.all().count()
    order_count=Order.objects.all().count()
    product_count=Product.objects.all().count()
    products=Product.objects.all()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.staff=request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form=OrderForm()

    context={
        'orders':orders,
        'form':form,
         'staff_count':staff_count,
        'order_count':order_count,
        'product_count':product_count,
        'products':products
    }
    return render(request,'dasboard/index.html',context)



@login_required
def staff(request):
    staff_users=User.objects.all()
    staff_count=User.objects.all().count()
    order_count=Order.objects.all().count()
    product_count=Product.objects.all().count()
    context={
        'staff_users':staff_users,
         'staff_count':staff_count,
        'order_count':order_count,
        'product_count':product_count,
    }
    
    return render(request, 'dasboard/staff.html',context)



@login_required
def product(request):
    staff_count=User.objects.all().count()
    order_count=Order.objects.all().count()
    product_count=Product.objects.all().count()
    if request.method =='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name=form.cleaned_data.get('name')
            messages.success(request,f'{product_name} has been added')
            return redirect ('dashboard-product')
    else:
        form=ProductForm()

    items=Product.objects.all() # using ORM
    # items=Product.objects.raw('SELECT * FROM dashboard_product') #raw SQL format
    context={'items':items,
    'form':form,
     'staff_count':staff_count,
        'order_count':order_count,
        'product_count':product_count,
            
    }
    return render(request, 'dasboard/product.html',context)





@login_required
def order(request):
    staff_count=User.objects.all().count()
    order_count=Order.objects.all().count()
    product_count=Product.objects.all().count()
    orders=Order.objects.all()
    context={
        'orders':orders,
         'staff_count':staff_count,
        'order_count':order_count,
        'product_count':product_count,
    }
    return render(request, 'dasboard/order.html',context)






@login_required
def staff_detail(request,pk):
    staff_users= User.objects.get(id=pk)
    context={
        'staff_users':staff_users,
    }
    return render (request,'dasboard/staff_detail.html',context)


