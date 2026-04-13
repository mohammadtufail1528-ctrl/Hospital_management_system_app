from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import login ,authenticate, logout


# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # ✅ Empty check
        if not username or not password:
            return render(request, 'user_signup.html', {'error': 'All fields are required'})

        # ✅ Duplicate check
        if User.objects.filter(username=username).exists():
            return render(request, 'user_signup.html', {'error': 'Username already exists'})

        # ✅ Create user
        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)
        return redirect('/deshboard')

    return render(request, 'user_signup.html')
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/deshboard')
        else:
            return render(request, 'user_login.html', {'error': 'Invalid username or password'})

    return render(request, 'user_login.html')
    
def logout_view(request):
    logout(request)
    return redirect('/login/')

