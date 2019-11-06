from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=30,
#         # HTML Tag와 동일
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'title',
#                 'placeholder': '제목을 입력해주세요...!',
#             }
#         )
#     )
#     content = forms.CharField(
#         label='내용',
#         # widget : Input Type 지정 -> Textarea / 알맞은 속성값 부여
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'content',
#                 'placeholder': '내용을 입력해주세요오오오오오',
#                 'rows': 5,
#                 'cols': 30,
#             }
#         )
#     )

# ModelForm
# 1. ModelForm 클래스를 상속받아 사용한다.
# 2. 메타데이터로 Model 정보를 건네주면, ModelForm이 자동으로 field에 맞춰 input을 생성해준다.
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'title',
                'placeholder': '제목 입력해라...'
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'content',
                'placeholder': '내용 입력해라...',
                'rows': 5,
                'cols': 30
            }
        )
    )

    # 메타데이터 -> 데이터의 데이터
    # ex) 사진 한장 (촬영장비이름, 촬영환경 등)
    class Meta:
        model = Article
        fields = ('title', 'content',)
        # fields = '__all__'