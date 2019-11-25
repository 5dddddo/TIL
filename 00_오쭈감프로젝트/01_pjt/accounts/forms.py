from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from accounts.models import MyUser


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        # User 클래스를 바로 사용하는 것이 아니라,
        # get_user_model() 을 사용해서  User 클래스를 참조한다
        model = MyUser
        # UserChangeForm -> User 클래스 -> AbstractUser 클래스
        # Django 공식문서 : user-model
        fields = UserCreationForm.Meta.fields + ('member_tel', 'member_emergency',
                                                 'member_msg', 'member_longitude', 'member_latitude',)


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'email',)
