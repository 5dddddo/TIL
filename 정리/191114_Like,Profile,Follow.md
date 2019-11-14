# 191114_Like / Profile / Follow

## 1. Like

> `User`는 여러 개의 `Article`에 좋아요 표시를 할 수 있고, `Article`은 여러 명의 `User`에게 좋아요를 받을 수 있다.

### 1.1 Model 설정

- ```
  blank=True
  ```

  - 최초 작성되는 글에는 좋아요가 없고, 글이 작성되더라도 좋아요를 받지 못할 수도 있다.
  - 이 옵션을 줘서 유효성 검사를 통과한다.
  - 실제 데이터베이스는 null이 들어가는게 아니라 빈 스트링(`''`) 형태로 들어간다.

```
# article/models.py

class Article(models.Model):
    ...
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles', blank=True)
```

- 현재 상황에서

   

  ```
  related_name
  ```

   

  설정은 필수

  - `like_users` 필드에 related_name을 쓰지 않으면, User 입장에서 article_set을 사용할 경우 user 필드를 갖고올지 like_users 필드를 갖고 올지 인식하지 못한다.
  - related_name 설정과 함께 해당 필드는 article_set과 같은 방식으로 호출하지 못하고, like_users 방식으로 호출해야 된다.

- 사용할 수 있는 ORM 기능(명령어)

  - `user.article_set.all()` : 유저가 작성한 게시글 전부 - 1:N
  - `user.like_articles.all()` : 유저가 좋아요 누른 게시글 전부 - M:N
  - `article.user` : 게시글 작성한 유저 - 1:N
  - `article.like_users` : 게시글 좋아요 누른 유저 전부 - M:N

### 1.2 View & URL

- ```
  exists()
  ```

   

  &

   

  ```
  filter()
  ```

  - `filter()` : 특정 조건에 맞는 레코드들을 가져온다.
  - `exists()` : 최소한 하나의 레코드가 존재하는지 여부를 말해준다.

- `get()` vs `filter()` -> 데이터가 없는 경우 에러 여부

```
# articles/views.py

@login_required
def like(request, article_pk):
    # 좋아요 누를 게시글 가져오기
    article = get_object_or_404(Article, pk=article_pk)
    # 현재 접속하고 있는 유저
    user = request.user
    # 게시글에 좋아요 누른 사람 목록에 현재 접속한 유저가 있을 경우 -> 좋아요 취소
    if article.like_users.filter(pk=user.pk).exists():
        article.like_users.remove(user)
    # 목록에 없을 경우가 -> 좋아요 누르기
    else:
        article.like_users.add(user)
    return redirect('articles:index')
# articles/urls.py

urlpatterns = [
    ...
    path('<int:article_pk>/like/', views.like, name='like'),
]
```

### 1.3 Template

#### 1.3.1 Template 분리 (`_article.html`)

- 모듈화한 템플릿은 제목 앞에 언더스코어(`_`) 붙여주는 것이 코딩 컨벤션!

  ```
  articles/
  	templates/
  		articles/
  			_article.html
  			index.html
  			...
  ```

- Bootstrap Card 컴포넌트를 사용해서 예쁘게 꾸며보자.

  - Bootstrap 공식 홈페이지 -> Documentation -> Cards

```
<!-- articles/index.html -->
...
<div class="row">
    {% for article in articles %}
    	{% include 'articles/_article.html' %}
    {% endfor %}
</div>
<!-- articles/_article.html -->
<div class="col-12 col-md-6">
    <p>
        여러분의 카드 디자인...
    </p>
</div>
```

#### 1.3.2 Font-Awesome 아이콘 적용 및 분기

> Font Awesome 홈페이지 가입 후 Kits로 들어가서 코드 복사

```
<!-- base.html -->
<!DOCTYPE html>
<html lang="ko">
<head>
  ...
  <!-- FontAwesome -->
  <script src="https://kit.fontawesome.com/여러분의 kits 코드번호" crossorigin="anonymous"></script>
</head>
<!-- articles/_article.html -->
...
<p class="card-text">
    <a href="{% url 'articles:like' article.pk %}">
        <!-- 사용자가 좋아요 누른 상태 -> 꽉찬 하트 -->
        {% if request.user in article.like_users.all %}
        <i class="fas fa-heart"></i>
        <!-- 안 누른 상태 -> 빈 하트 -->
        {% else %}
        <i class="far fa-heart"></i>
        {% endif %}
    </a>
    ...
</p>
...
```

## 2. Profile 페이지

> 각 유저마다 프로필 페이지를 만들어주자.

- User에 대해서 CRUD 로직을 구현한다고 생각하면, READ(Detail)에 속한다.

### 2.1 View & URL

- User에 대한 CRUD 로직 대부분을 accounts 앱에서 구현했으므로, Profile 페이지 역시 accounts 앱에 구현해보자.

```
# accounts/views.py
# accounts/urls.pyh
```

### 2.2 Template

```
<!-- profile.html -->
```

## 3. Follow

- Follow는 User와 User의 M:N관계다.
- 장고가 제공하고 있는 User 모델을 대체해서 사용한다. 처음부터 User 모델을 만드는게 아니라, 장고가 개발자들이 자신만의 User 모델을 만들 수 있도록 제공해준다.
  - `AbstractUser`

### 3.1 User 모델 대체하기

```
# accounts/models.py
```