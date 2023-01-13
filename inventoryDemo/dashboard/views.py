from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   # return HttpResponse("<h1>Index page</h1>")
    return render(request,'dasboard/index.html')

def staff(request):
    return render(request, 'dasboard/staff.html')

def product(request):
    return render(request, 'dasboard/product.html')
def order(request):
    return render(request, 'dasboard/order.html')
def profile(request):
    return render(request, 'dasboard/profile.html')