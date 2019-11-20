from django import forms
from .models import Article,Comment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class': 'title',
                'placeholder': '제목을 입력하시오',
            }
        )
    )
    content = forms.CharField(
        label='내용 입력 하세요',
        widget=forms.Textarea(
            attrs={
                'class':'content',
                'placeholder':'내용입력해',
                'rows':5,
                'cols':30,
            }
        )
    )

    #메타데이터 : 데이터의 데이터
    #ex) 사진 한장 ( 촬영장비이름, 촬영환경 등 )
    class Meta:
        model = Article
        fields = 'title','content'      #원하는것만 필드에 나타나게 할 수 있다 ( 'title','content',)


class CommentForm(forms.ModelForm):
   
    content = forms.CharField(
        label='댓글',
        widget=forms.Textarea(
            attrs={
                'class':'content',
                'placeholder':'댓글입력해',
                'rows':1,
                'cols':30,
            }
        )
    )
    class Meta:
        model = Comment
        fields = ('content',)      #원하는것만 필드에 나타나게 할 수 있다 ( 'title','content',)

