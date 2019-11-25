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
                                                 'member_msg',)
        
        member_tel = forms.RegexField(
            regex=r'^\d{3}-\d{3,4}-\d{4}$', error_messages={'invalid': '휴대전화 형식은 xxx-xxxx-xxxx입니다.'},)
        member_emergency = forms.RegexField(
            regex=r'^\d{3}-\d{3,4}-\d{4}$',  error_messages={'invalid': '휴대전화 형식은 xxx-xxxx-xxxx입니다.'},)
        
        readonly = ('username',)
        labels = {
            'member_tel': '휴대폰 번호',
            'member_emergency': '비상 번호',
            'member_msg': '비상 메시지'
        }


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2',
                  'member_tel', 'member_emergency', 'member_msg',)

        member_tel = forms.RegexField(
            regex=r'^\d{3}-\d{3,4}-\d{4}$', error_messages={'invalid': '휴대전화 형식은 xxx-xxxx-xxxx입니다.'},)
        member_emergency = forms.RegexField(
            regex=r'^\d{3}-\d{3,4}-\d{4}$',  error_messages={'invalid': '휴대전화 형식은 xxx-xxxx-xxxx입니다.'},)

        labels = {
            'member_tel': '휴대폰 번호',
            'member_emergency': '비상 번호',
            'member_msg': '비상 메시지'
        }
