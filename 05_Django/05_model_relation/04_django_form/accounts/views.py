from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Create your views here.
# Authentication(인증) -> 신원 확인
#    - 자신이 누구라고 주장하는 사람의 신원을 확인하는 것


def signup(request):
    # 이미 로그인 되어있는 친구가 회원가입 하려고 하면
    if request.user.is_authenticated:
        return redirect('articles:index')


    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm
    context = {
        'form' : form
    }
    return render(request, 'accounts/auth_form.html', context)



def login(request):
    # 이미 로그인 되어있는 친구가 로그인 하려고 하면
    if request.user.is_authenticated:
        return redirect('articles:index')


    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # return redirect('articles:index')
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)
    

def logout(request):
    auth_logout(request)
    return redirect('articles:index')


@require_POST
def delete(request):
    request.user.delete()
    return redirect('articles:index')

@login_required
def update(request):
    if request.method =='POST':
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {'form':form}
    return render(request, 'accounts/auth_form.html', context)

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
    context = {'form':form}
    return render(request, 'accounts/auth_form.html',context)

def profile(request, username):
    person = get_object_or_404(get_user_model(), username=username)
    context = {
        'person' : person
    }
    return render(request, 'accounts/profile.html', context)()
