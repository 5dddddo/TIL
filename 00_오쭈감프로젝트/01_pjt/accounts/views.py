from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from .forms import CustomUserChangeForm
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model


def index(request):
    return render(request, 'accounts/index.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('safeLoad:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        # UserCreationForm(request.POST)
        if form.is_valid():
            # 회원가입 하면 바로 로그인으로 넘겨버리기
            user = form.save()
            auth_login(request, user)
            return redirect('safeLoad:index')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/auth_form.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('safeLoad:index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'safeLoad:index')

    return redirect('safeLoad:index')


# def login(request):
#     if request.user.is_authenticated:
#         return redirect('safeLoad:index')

#     if request.method == 'POST':

#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             auth_login(request, form.get_user())
#             return redirect(request.GET.get('next') or 'safeLoad:index')
#     else:
#         form = AuthenticationForm()
#     context = {'form': form}
#     return render(request, 'accounts/auth_form.html', context)


def logout(request):
    auth_logout(request)
    return redirect('safeLoad:index')


# 회원정보 수정
@login_required
def update(request):
    if request.method == 'POST':
        # 첫번째 : 사용자가 입력한 데이터 # 두번째 : 접속하고 있는 회원 instance인자로 넘김
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('safeLoad:index')
    else:
        # form = UserChangeForm(instance=request.user)
        form = CustomUserChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'accounts/auth_form.html', context)

# 로그인 한 상태에서만 폼을 보여야 하므로 login_required 데코레이터 사용
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form': form}
    return render(request, 'accounts/auth_form.html', context)
