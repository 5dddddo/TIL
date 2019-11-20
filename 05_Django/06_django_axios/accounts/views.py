from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import CustomUserChangeForm, CustomUserCreationForm


# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')

# Authentication(인증) ->신원확인
# - 자신이 누구라고 주장하는 사람의 신원을 확인하는 것

# Auth CRUD : CREATE
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
                # UserCreationForm(request.POST)
        if form.is_valid():
            #회원가입 하면 바로 로그인으로 넘겨버리기
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()  
    context = {'form':form}
    return render(request, 'accounts/auth_form.html', context)


def login(request):
    #request에 user가 돌아다닌다
    #이미 로그인되어있는 친구가 get으로 로그인 들어오려고 하면 index로 redirect시켜버리자
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method =='POST':
        # 세션 관련된 정보를 받기 위해 request를 받는다
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # return redirect('articles:index')
            # next에 담겨있는 이 경로로 보내든지 아니면 index로 보내
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context ={'form':form}
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')

@require_POST
def delete(request):
    request.user.delete()
    return redirect('articles:index')


# 회원정보 수정
@login_required
def update(request):
    if request.method =='POST':
        # 첫번째 : 사용자가 입력한 데이터 # 두번째 : 접속하고 있는 회원 instance인자로 넘김
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        # form = UserChangeForm(instance=request.user)
        form = CustomUserChangeForm(instance=request.user)
    context={'form':form}
    return render(request, 'accounts/auth_form.html', context)



#로그인 한 상태에서만 폼을 보여야 하므로 login_required 데코레이터 사용
@login_required
def change_password(request):
    if request.method =='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {'form':form}
    return render(request, 'accounts/auth_form.html',context)


def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {'person':person}
    return render(request, 'accounts/profile.html', context) 