from django.shortcuts import render
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Foydalanuvchi ro'yxatdan o'tkazilganda avtomatik ravishda tizimga kiring
            login(request, user)
            return redirect('register')  # O'zgartirishingiz kerak bo'lgan boshqa sahifa nomi
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})