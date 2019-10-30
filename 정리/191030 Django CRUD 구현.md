# 191030 Django CRUD 구현

## 0. 사전 작업

#### 0.1 프로젝트 생성

``` bash
$ django-admin startproject config .
```

#### 0.2 애플리케이션 생성

``` BASH
$ python manage.py startapp articles
```

``` BASH
# settings.py : 출생신고 까먹지말자........
INSTALLED_APPS = [
    'articles',
    ...
]
```

#### 0.3 URL 분리 (위임)

``` python
# config/urls.py
from django.urls import path,include

urlpatterns = [
    # articles/로 시작하는 경로는
    # articles의 urls.py에서 처리하기
    path('articles/',include('articles.urls')),
]
```

- **articles/urls.py** 파일 생성

<br>

#### 0.4 템플릿 경로 커스터마이징 + base.html 만들기

- 템플릿 경로 커스터마이징

  - django는 애플리케이션 내부의 templates이 Default 값으로 설정 되어 있음

  - config 폴더 안에 있는 templates 폴더로 경로 변경

    - config /settings.py

    ``` python
    TEMPLATES = [
        {	...
         # config 폴더의 templates 폴더를 default 경로로 설정
            'DIRS': [os.path.join(BASE_DIR,'config','templates')],
    		...   
        }
    ]
    ```

    <br>

- 아래 코드 템플릿이 깨질 경우 base.html에 Bootstrap CSS, JS 파일 적용했는지 확인

``` python
# base.html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width={device-width}, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>장고 CRUD</title>

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>

<body>
  <div class="container">
    {% block body %}
    {% endblock body %}
  </div>
  <!-- Bootstrap JS -->
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous">
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
    integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous">
  </script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
    integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous">
  </script>

</body>
</html>
```

<br>

#### 0.5 데이터 모델링

- **articles/models.py**

  ```python
  class Article(models.Model):
      title = models.CharField(max_length=40)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      
      # 객체 표시 형식 수정
      def __str__(self):
          return f'[{self.pk}] {self.title}'
  ```

- `makemigrations` : 설계도 만들기

  ```bash
  $ python manage.py makemigrations
  03_django_crud/
      config/
      articles/
          migrations/
              0001_initial.py
  ```

- `migrate` : 실제 DB에 반영하기

  ```bash
  $ python manage.py migrate
  ```

- **추가 정보**

  - `showmigrations` : makemigrations를 통해 만든 설계도가 실제 DB에 반영된 상태인지 아닌지 확인

  - `sqlmigrate` : 실제 DB에 반영하기 전 SQL 쿼리문으로 바뀐 모습 확인

    ```bash
    $ python manage.py sqlmigrate articles 0001
    ```

<br>

## 1. CREATE

- 기본적으로 두 개의 뷰 함수로 구성

  - 사용자에게 HTML Form을 던져줄 함수

  - HTML Form에서 데이터를 전달 받아서 실제 DB에 저장하는 함수

  - #### 일단, GET 방식으로 구현해보자!

  ``` python
  # articles/views.py
  
  def new(request):
      return render(request,'articles/new.html')
  
  def create(request):
      title = request.GET.get('title')
      content = request.GET.get('content')
      article = Article(title = title, content = content)
      article.save()
  
      return render(request, 'articles/create.html')
  ```

  ``` html
  <!-- templates/articles/new.html -->
  
  {% extends 'base.html' %}
  {% block body %}
  <h1 class="text-center">NEW</h1>
  <form action="/articles/create/" method="GET">
    TITLE : <input type="text" name="title"><br>
    CONTENT : <textarea name="content" cols="30" rows="10"></textarea> <br>
    <input type="submit">
  </form>
  <hr>
  <a href="/articles/"> [BACK]</a>
  {% endblock body %}
  
  <!-- templates/articles/create.html -->
  
  {% extends 'base.html' %}
  
  {% block body %}
  <h2> 글 작성이 완료되었습니다! <h2>
  {% endblock body %}
  ```

  <br>

- 데이터가 정상적으로 저장됐는지 확인하기 위해 **admin 페이지**로 들어가보자!

  - **admin 계정 생성**

  ```bash
  $ python manage.py createsuperuser
  ```

  - admin.py 등록

  ``` python
  from django.contrib import admin
  from .models import Article
  
  class ArticleAdmin(admin.ModelAdmin):
      list_display = ('pk','title','content','created_at','updated_at',)
  
  admin.site.register(Article,ArticleAdmin)
  ```

<br>

- 메인 페이지에서 게시글 목록 출력하기 (**Read - index** 로직)

  ``` python
  # articles/views.py
  def index(request):
      articles = Article.objects.all()[::-1]
      context = {'articles' : articles}
      return render(request, 'articles/index.html',context)
  ```

  ``` html
  <!-- templates/articles/index.html -->
  {% extends 'base.html' %}
  {% block body %}
  <h1 class="text-center"> Articles </h1>
  <a href="/articles/new/">[NEW]</a>
  <hr>
  
  {% for article in articles %}
  <p>글 번호 : {{article.pk}} </p>
  ...
  <p>수정 시각 : {{article.updated_at}}</p>
  <hr>
  {% endfor %}
  {% endblock body %}
  ```

<br>

- #### 게시글 작성 요청 방식을 GET에서 **POST** 방식으로 바꿔보자!

  - 현재는 GET 요청으로 보내고 있어서 쿼리 스트링에 데이터가 노출 됨

  - 이는 서버의 데이터가 노출될 위험이 있고, URL 경로로도 게시글 작성이 가능해 서버 폭파의 위험성 증가함

  - POST 요청으로 바꾸어 HTTP body의 내용을 숨기고 작성자의 신원을 확인하는 절차 거침

    ``` python
    # articles/views.py
    def create(request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()
        return render(request, 'articles/create.html')
    ```

  - 게시글 작성을 완료한 후 '게시글 작성을 완료했어요!' 라는 문구가 뜨도록 구현

    - DB에 게시글 작성이 완료되면 메인 페이지로 **Redirect** 시키자!

    ```python
    # articles/views.py
    from django.shortcuts import render, redirect
    def create(request):
        title = request.POST.get('title')
        content = request.POST.get('content')
    
        article = Article(title=title, content=content)
        article.save()
        
        # render 는 views에서 index.html만 찾아서 뿌려주는 역할
        # index 함수를 실행하지 않음
        # 함수까지 실행하려면 redirect 함수 사용!
        return redirect('/articles/')
    ```

    <BR>

    - ##### POST 설정 시 CSRF_TOKEN 설정 : 작성자의 신원 확인 절차

    ```html
    <!-- templates/articles/new.html -->
    {% extends 'base.html' %}
    {% block body %}
    <h1 class="text-center">NEW</h1>
    <form action="/articles/create/" method="POST">
    {% csrf_token %}
      TITLE : <input type="text" name="title"><br>
      CONTENT : <textarea name="content" cols="30" rows="10"></textarea> <br>
      <input type="submit">
    </form>
    <hr>
    <a href="/articles/"> [BACK]</a>
    {% endblock body %}
    ```

  <br>

## 2. READ - detail 페이지

- 게시글 목록이 출력되는 메인 페이지에서 글 내용, 수정 시각 등 모든 정보를 보여줄 필요 없음

- 메인 페이지에서는 글 번호, 제목과 같은 기본적인 내용만 출력

- 사용자가 클릭했을 때, 게시글 상세 정보 페이지로 이동하도록 하자

  ``` python
  # articles/urls.py
  
  # Variable Routing 적용
  # 사용자가 게시글을 조회할 때 URL 주소 : ../articles/1, ../articles/2로 조회하도록 함
  urlpatterns = [
      path('<int:article_pk>/',views.detail),
      ...
  ]
  ```

  ``` python
  # articles/views.py
  
  # 사용자가 요쳥을 보낸 URL로부터 게시글의 PK 값을 건네받음
  # 게시글 상세정보를 가져오는 함수
  def detail(request, article_pk):
      article = Article.objects.get(pk=article_pk)
      context = {'article': article}
      return render(request, 'articles/detail.html', context)
  
  ```

  ``` html
  <!-- detail.html -->
  {% extends 'base.html' %}
  {% block body %}
  <h1 class="text-center">Detail</h1>
  <p>글 번호 : {{article.pk}}</p>
  <p>글 제목 : {{article.title}}</p>
  <p>글 내용 : {{article.content}}</p>
  <p>생성 시각 : {{article.created_at}}</p>
  <p>수정 시각 : {{article.updated_at}}</p>
  <a href = "/articles/"></a>
  {% endblock body %}
  ```

  ``` html
  <!-- index.html -->
  {% extends 'base.html' %}
  {% block body %}
  <h1 class="text-center"> Articles </h1>
  <a href="/articles/new/">[NEW]</a>
  <hr>
  
  {% for article in articles %}
  
  <p>{{article.pk}} {{article.content}}</p>
  <a href="/articles/{{article.pk}}">[DETAIL]</A>
  <hr>
  {% endfor %}
  {% endblock body %}
  ```

## 3. UPDATE

## 4. DELETE