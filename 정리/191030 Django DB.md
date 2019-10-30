# 191030 Django DB

-  Django MTV 패턴

  - **Model** : 특정한 데이터의 구조(모양)에 대한 정보를 가지고 있음

    ​			  데이터의 모양을 정의하는곳

    ​			  하나의 모델 클래스는 실제 DB에는 하나의 테이블로 mapping

    ​			  컬럼들에 대한 정보, 해당 데이터에 대한 정보를 정의하는 곳

  - Template

  - View

    

- Model 로직
  - DB 컬럼(열)과 어떠한 타입으로 정의할 것인지에 대한 정보를

    `django.db.models` 라는 곳에서 상속받아서 정의

  - 모든 필드들은 `NOT NULL` 조건이 붙음

<br>

### 1.1 Migration

- **makemigrations**
  - 실제 DB 테이블을 만들기 전에 설계도를 그려보는 작업
  - migrations 폴더에서 확인해 볼 수 있음
    - 0001_ititial.py

- `sqlmigrate`

  - DB에 실제로 반영하기 전에 SQL문으로 바뀐 모습을 확인해볼 수 있음

  ![1572396707837](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572396707837.png)

- showmigrations 

  - migration 설계도를 작성했는데, 이 설계도가 실제 DB에 반영되었는지 확인

  ![1572396789669](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572396789669.png)

- migrate

  - makemigrations로 만든 설계도를 실제 DB(sqlite3)에 반영함
  - 모델의 변경사항과 DB 스키마에 동기화
  - 반영되면 [X] 표시

  ![1572397941529](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572397941529.png)

  ![1572397965718](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572397965718.png)

<br>

- Sqlite exploror

  

  ![1572399095956](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572399095956.png)

### 2. ORM - CRUD

> 앞으로 DB에 SQL 쿼리문을 날려서 데이터를 조작하는 것이 아니라,
>
> **ORM을 통해 클래스의 인스턴스 객체로 DB를 조작**함

<BR>

- ORM을 리턴되는 형식

  - QuerySet : 다수의 객체가 담기 ( Python의 list와 비슷 )
  - Query : 단일 객체

- 모델명.objects.명령

  - objects : 모델 클래스 정보를 토대로 실제 DB에 쿼리(SQL)를 날려서

    ​			    DB와 의사소통하는 통역사(매니저) 역할

    

- `pip install ipython`

- `python manage.py shell`

  ![1572399956858](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572399956858.png)

![1572401689284](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572401689284.png)

![1572400408596](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572400408596.png)



- ORM을 리턴하는 형식
  - QuerySet : 다수의 객체가 담김 (파이썬 리스트 다루는 것과 비슷)
  - Query : 

#### 2.1 Create

```sqlite
# 첫번째 방법
article = Article()
article.title = 'first'
article.content = 'django'
article.save()
	
# 두번째 방법 : 함수에서 키워드 인자 넘겨주는 방식
article = Article(title='second',content='django')
article.save()

# 세번째 방법 : 쿼리셋 객체 생성과 DB 저장을 한 번에 해결
article.objects.create(title='third',content='django')
```

``` sqlite
# 유효성 검증
article.full_clean()
```



- 객체를 표시하는 형식 커스터 마이징하기

  - 02_django_orm_curd - articles (app) - models.py

  ``` python
  # shell 나갔다가 다시 실행
  def __str__(self):
  	return f'[{self.pk}]: {self.title}'
  ```

  - python manage.py shell

  ``` sqlite
  # 결과 확인
  from articles.models import article
  
  In[]: Article.objects.all()
  Out[]: <QuerySet [<Article: [1]: first>, <Article: [2]: third>, <Article: [3]: second>]>
  ```

<Br>

#### 2.2 Read

- `Article.objects.all()`

- `res = Article.objects.filter(조건)`

  - 복수 개의 결과가 return 될 수 있으므로 QuerySet으로 return 됨

  ``` sqlite
  In[]: res = Article.objects.filter(title='first')
  
  In[]: res
  Out[]: <QuerySet [<Article: [1]: first>, <Article: [4]: first>]>
  
  In[]: type(res)
  Out[]: django.db.models.query.QuerySet
  ```

  

- `res = Article.objects.filter(조건).first()`

  - 한 개의 Query만 return

  ``` sqlite
  In[]: res = Article.objects.filter(title='first').first()
  In[]: res
  Out[]: <Article: [1]: first>
  ```

<br>

- ` articles = Article.objects.get(조건)`

  - get()은 한 개의 결과만 return 되는 함수기 때문에 pk를 조건으로 찾아야 함

  ``` sqlite
  In []: article = Article.objects.get(pk=2)
  In []: article
  Out[]: <Article: [3]: second>
  ```

  <br>

  - QuerySet이 반환되는 조건으로 get() 사용하면 **Error!**

  ``` sqlite
  In [28]: articles = Article.objects.get(title='first')
  
  ------------------ Error ------------------
  
  MultipleObjectsReturned: get() returned more than one Article -- it returned 2!
  ```

  <br>

- 정렬하기

  - `articles = Article.objects.order_by('-조건') `: 내림차순

    ``` sqlite
    In []: articles = Article.objects.order_by('-pk')
    
    In []: articles
    Out[]: <QuerySet [<Article: [4]: first>, <Article: [3]: second>, <Article: [2]: third>, <Article: [1]: first>]>
    
    ```

  - `articles = Article.objects.order_by('조건')`: 오름차순

    ```sqlite
    In []: articles = Article.objects.order_by('pk')
    
    In []: articles
    Out[]: <QuerySet [<Article: [1]: first>, <Article: [3]: second>, <Article: [4]: first>]>
    ```

    <br>

- python의 list 타입처럼 사용 가능

  ``` sqlite
  In []: res = Article.objects.all()[1:3]
  
  In []: type(res)
  Out[]: django.db.models.query.QuerySet
  ```

  

- 특정 문자열 포함하는 객체 찾기

  ``` sqlite
  In []: Article.objects.filter(title__contains='fir')
  Out[]: <QuerySet [<Article: [1]: first>, <Article: [4]: first>]>
  ```

- 특정 문자열로 시작하는 객체 찾기

  ``` sqlite
  In []: Article.objects.filter(title__startswith='fir')
  Out[]: <QuerySet [<Article: [1]: first>, <Article: [4]: first>]>
  ```

- 특정 문자열로 끝내는 객체 찾기

  ``` sqlite
  In []: Article.objects.filter(title__startswith='fir')
  Out[]: <QuerySet [<Article: [1]: first>, <Article: [4]: first>]>
  
  In []: Article.objects.filter(title__endswith='d')
  Out[]: <QuerySet [<Article: [2]: third>, <Article: [3]: second>]>
  ```

#### 2.3 Update

``` sqlite
# 1. 수정할 인스턴스 가져오기
article = Article.objects.get(pk=2)

# 2. 인스턴스 값 확인하기
article.title
'third'

# 3. 인스턴스 값 수정하기
article.title = 'hello'

# 4. 인스턴스 값 확인하기
article.title
'hello'

# 5. DB에 반영하기
article.save()
```

![1572402552334](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572402552334.png)

#### 2.4 Delete

``` sqlite
In []: article.delete()
Out[]: (1, {'articles.Article': 1})
```

![1572402597006](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572402597006.png)



### 3. admin

#### 3.1 user 등록

- `$ python manage.py createsuperuser` 

- 실행화면

  ``` bash
  $ python manage.py createsuperuser
  Username (leave blank to use 'student'): admin
  Email address:
  Password:
  Password (again):
  The password is too similar to the username.
  This password is too short. It must contain at least 8 characters.
  This password is too common.
  Bypass password validation and create user anyway? [y/N]: y
  Superuser created successfully.
  ```

<br>

- http://127.0.0.1:8000/admin

![1572408957210](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572408957210.png)

- admin site에 Article 등록하기

  - articles - admin.py

    ``` python
    # articles - admin.py
    from django.contrib import admin
    from .models import Article
    
    # Register your models here.
    
    admin.site.register(Article)
    ```

  ![1572409019224](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572409019224.png)



- list_display 
  - article 출력하기

![1572409667341](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572409667341.png)

``` python
from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk','title','content','created_at','updated_at',)
    
admin.site.register(Article,ArticleAdmin)
```

![1572409798495](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572409798495.png)

- list_filter(조건,)

![1572410088429](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572410088429.png)

- list_display_links(조건,)

  ![1572410178454](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572410178454.png)

- list_editable=(조건,)

![1572410588590](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572410588590.png)

- list_per_page = 개수

![1572410620796](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572410620796.png)

--------------------

<br>

#### 3.4 shell 실행 시 자동 import하기

- shell 재실행 시 마다 `from articles.models import Article` 해주어야 함

- `pip install django-extensions`

- config - settings.py

  ```python
  INSTALLED_APPS = [
      ...
      # Third party apps
      'django-extensions',
      ...
  ```

- `python manage.py shell_plus`

  ![1572412480710](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1572412480710.png)