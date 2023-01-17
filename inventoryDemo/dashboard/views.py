from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
   # return HttpResponse("<h1>Index page</h1>")
    return render(request,'dasboard/index.html')



@login_required
def staff(request):
    return render(request, 'dasboard/staff.html')



@login_required
def product(request):
    return render(request, 'dasboard/product.html')




@login_required
def order(request):
    return render(request, 'dasboard/order.html')



