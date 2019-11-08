# 191106_Django form

### 1. 사전 준비

> Django Form을 적용하기 전, 이때까지 우리가 학습했던 HTML Form으로 앱을 구현해보자.

- **프로젝트 생성**

  ```bash
  $ mkdir 04_django_form
  $ cd 04_django_form
  ```

  ```bash
  $ django-admin startproject config .
  ```

- **앱 생성**

  ```
  $ python manage.py startapp articles
  ```

- **Article Model**

  ```python
  # models.py
  from django.db import models
  
  class Article(models.Model):
      title = models.CharField(max_length=20,blank=True)
      content = models.TextField(blank=True)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      def __str__(self):
          return f'[{self.pk}] {self.title}'
  ```

- **URL 설정**

  ```python
  # config/urls.py
  from django.contrib import admin
  from django.urls import path,include
  
  urlpatterns = [
      path('articles/',include('articles.urls')),
      path('admin/', admin.site.urls),
  ]
  ```

  ```python
  # articles/urls.py
  from django.urls import path
  from . import views
  
  app_name = 'articles'
  urlpatterns = [
      path('', views.index, name='index'),
      path('create/', views.create, name='create'),
      path('<int:article_pk>/', views.detail, name='detail'),
      path('<int:article_pk>/delete/', views.delete, name='delete'),
      path('<int:article_pk>/update/', views.update, name='update'),
  ]
  ```

- **base.html 생성** (부트스트랩 적용X)

- **Index 페이지** (-> 모든 게시글 보여주기)

  ```python
  # views.py
  def index(request):
      articles = Article.objects.all()[::-1]
      context = {'articles': articles}
      return render(request, 'articles/index.html', context)
  ```

  ```html
  <!-- index.html -->
  {% extends 'articles/base.html' %}
  {% block body %}
  <h1>Articles</h1>
  <a href="{% url 'articles:create' %}">[NEW]</a>
  <hr>
  {% for article in articles %}
  <p>번호: {{ article.pk }}</p>
  <p>제목: {{ article.title }}</p>
  <a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>
  {% endfor %}
  {% endblock %}
  ```

- **Detail 페이지**

  ```
  # views.py
  def detail(request, article_pk):
      pass
  ```

  ```
  <!-- detail.html -->
  ```



## 2. Django Form

>  Django에서 제공하는 Form 클래스를 이용해서 편리하게 폼 정보를 관리하고 유효성 검증을 진행하고, 비유효 field에 대한 에러 메시지를 결정한다. 
>
> 즉, HTML으로 Form 입력을 관리하던 것을 Django에서 제공하는 Form 클래스로 바꿔보는 작업을 해보자.

- **Form의 장점(-> 자동화)**
  - blank=True 와 같은 옵션을 따로 지정해주지 않았으면, HTML 태그에 required 옵션을 자동으로 붙여줌
  - 기존에 max_length와 같은 조건을 어길 경우, 에러 페이지를 출력
    - Django form을 써서 에러 메시지 출력함


``` python
# forms.py
from django import forms
class ArticleForm(forms.Form):
    title = forms.CharField(max_length=30,
                            # label : HTML tag와 동일한 기능
                            label='제목',
                            # widget : Input Type 지정 -> Textarea / 알맞은 속성값 부여
                            widget=forms.TextInput(
                                attrs={'class': 'title',
                                       'placeholder': '제목을 입력해주세요...!',
                                      }))
    content = forms.CharField(label='내용',
                              widget=forms.Textarea(
                                  attrs={'class': 'content',
                                      	 'placeholder': '내용을 입력해주세요옥',
                                         'rows': 5,
                                         'cols': 30,
                                  	    }))
```

``` python
# views.py
from IPython import embed

def create(request):
    # POST 요청 -> 데이터를 받아서 DB에 저장
    if request.method == 'POST':
        # Binding 과정
        # 폼 인스턴스를 생성하고, 전달받은 데이터를 채운다.
        # 인스턴스에 데이터를 채워서, 유효성 검증을 진행한다.
        form = ArticleForm(request.POST)
        embed()
        if form.is_valid():
            # 검증이 끝난 데이터를 cleaned_data를 통해 딕셔너리 형태로 변환한다.
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article = Article.objects.create(title=title, content=content)
        return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    # form으로 전달받는 형태가 2가지
    # 1. GET요청 -> 비어있는 폼 전달
    # 2. 유효성 검증 실패 -> 에러 메시지를 포함한 채로 폼 전달
    context = {'form': form}
    return render(request, 'articles/create.html', context)
```

``` shell
In [1]: form
Out[1]: <ArticleForm bound=True, valid=Unknown, fields=(title;content)>

In [2]: request.POST
Out[2]: <QueryDict: {'csrfmiddlewaretoken': ['U1J7RiHKAesPTziSAwvboujPOKqSrouK01pu2DMCXZ6EgiSDLwjJehiLLhOMzHsl'], 'title': ['dfsdfsd'], 'content': ['sdfsdf']}>

In [3]: type(form)
Out[3]: articles.forms.ArticleForm

In [4]: form.is_valid()
Out[4]: True

In [5]: form
Out[5]: <ArticleForm bound=True, valid=True, fields=(title;content)>

In [6]: form.cleaned_data
Out[6]: {'title': 'dfsdfsd', 'content': 'sdfsdf'}

In [7]: type(form.cleaned_data)
Out[7]: dict

In [8]: form.cleaned_data.get('title')
Out[8]: 'dfsdfsd'

In [9]: exit()
```

- 실행 결과

  ![1573015084400](assets/1573015084400.png)



## ERROR 500

- 문제 : 사용자가 이상한 URL 주소를 쳤을 때, ERROR 404가 아니라 500이 뜸

![1573015500518](assets/1573015500518.png)

![1573015355693](assets/1573015355693.png)

- 해결

- **get_object_or_404**

  - 500 에러는 내부 서버 오류로, '서버에 오류가 발생하여 요청을 처리할 수 없다'는 의미다. 예를 들어 articles/38513858135와 같이 존재하지 않는 상세정보 페이지를 요청하면 500 에러가 발생한다.
  - 하지만 이 경우엔 사용자의 요청이 잘못된 경우이기 때문에 '서버에 존재하지 않는 페이지에 대한 요청'이라는 의미를 가진 404 에러를 돌려주어야 한다.
    - 500 에러를 돌려주면 "선생님, 깃헙 폭파됐는데요?"라는 말이 나올거고, 404 에러를 돌려주면 "아, 선생님이 주소를 잘못 줬거나 내가 잘못 쳤구나..."라는 말이 나올 것.
  
  ``` python
  from django.shortcuts import ..., get_object_or_404
  
  def detail(request, article_pk):
      article = get_object_or_404(Article,pk = article_pk)
    # article = Article.objects.get(pk=article_pk)
      context = {'article': article, }
      return render(request, 'articles/detail.html', context)
  ```
  
  ![1573015472100](assets/1573015472100.png)



### DELETE

```python
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)
```

### UPDATE

```python
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        # 두번째 인자로 article 인스턴스를 넘겨준다. (instance 키워드 인자!)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        # article 인스턴스를 넘겨주어 폼 초기값을 채운다.
        form = ArticleForm(instance=article)
    context = {'form': form}
    return render(request, 'articles/form.html', context)
```

------

## 3. Django ModelForm

- 개념

  - Django의 큰 특징 중 하나
  - Model 클래스 정의와 비슷하게 Form 클래스를 선언할 수 있다.

- 역할

  1. HTML 입력 폼 생성 : `as_p()`, `as_table()`
  2. 유효성 검증 : `is_valid()`
  3. 검증 통과한 값 딕셔너리로 제공 : `cleaned_data`

- `Form` vs `ModelForm`

  ```python
  # forms.py
  
  # Django Form
  class ArticleForm(forms.Form):
      title = forms.CharField()
      content = forms.CharField()
  
  # Django ModelForm
  # Django가 건네받은 모델을 기준으로 폼 양식에 필요한 대부분을 전부 만들어준다.
  class ArticleForm(forms.ModelForm):
      class Meta:
          model = Article
          fields = '__all__'
  ```

- 전체 코드

  ```python
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
  
      # 메타데이터: 데이터의 데이터
      # ex) 사진 한장 (-> 촬영장비이름, 촬영환경 등)
      class Meta:
          model = Article
          fields = ('title', 'content',)
          # fields = '__all__'
  ```