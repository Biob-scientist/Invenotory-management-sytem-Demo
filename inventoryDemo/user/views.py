from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm,UserUpadteForm,ProfileUpdateForm
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account has been created for {username}. Login to continue')
            return redirect('user-login')
    else:
        form=CreateUserForm()

    context={'form':form,}
    return render(request, 'user/register.html',context)
    
def profile(request):
    return render(request, 'user/profile.html')
    
def profile_update(request):
    if request.method=='POST':
        userform=UserUpadteForm(request.POST,instance=request.user)
        profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if userform.is_valid() and profile_form.is_valid():
            userform.save()
            profile_form.save()
            return redirect('user-profile')
    else:
        userform=UserUpadteForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user.profile)

    context={
        'userform':userform,
        'profile_form':profile_form
    }
    
    return render(request, 'user/profile_update.html',context)