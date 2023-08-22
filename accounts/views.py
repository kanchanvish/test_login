
from django.shortcuts import render, redirect
from .models import User, Referral
from django.contrib.auth.decorators import login_required
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create(username=username, email=email, password=password)
        referral_code = request.POST.get('referral_code')
        if referral_code:
            try:
                referrer = User.objects.get(username=referral_code)
                Referral.objects.create(referrer=referrer, referred_user=user)
            except User.DoesNotExist:
                pass
        return redirect('login')
    return render(request, 'accounts/register.html')

def login(request):
    return render(request, 'accounts/login.html')


@login_required
def dashboard(request):
    user = request.user
    referrals = Referral.objects.filter(referrer=user)
    return render(request, 'accounts/dashboard.html', {'referrals': referrals})