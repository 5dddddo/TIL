# 191121_Pagination & Search

## 1. Pagination

- 게시글 페이지 나누기! 

### 1.1 View

- `articles/views.py`

  ``` python
  from django.core.paginator import Paginator
  
  def index(request):
      articles = Article.objects.all()
      # 1. articles를 Paginator에 넣기
      # Paginator(전체 리스트, 보여줄 갯수)
      paginator = Paginator(articles,4)
      
      # 2. 사용자가 요청한 Page 가져오기
      page = request.GET.get('page')
      
      # 3. 해당하는 page의 article만 가져오기
      articles = paginator.get_page(page)
      print(dir(articles))
      print(dir(articles.paginator))
      context = {'articles': articles}
      return render(request, 'articles/index.html', context)
  ```

- `dir(articles)`

  ```
  ['__abstractmethods__', '__class__', '__contains__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_abc_impl', 'count', 'end_index', 'has_next', 'has_other_pages', 'has_previous', 'index', 'next_page_number', 'number', 'object_list', 'paginator', 'previous_page_number', 'start_index']
  ```

- `dir(articles.paginator)`

  ```
  ['__abstractmethods__', '__class__', '__contains__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_abc_impl', 'count', 'end_index', 'has_next', 'has_other_pages', 'has_previous', 'index', 'next_page_number', 'number', 'object_list', 'paginator', 'previous_page_number', 'start_index']
  ```
  - html에서 이용!

- 실행 시 `127.0.0.1:8000/articles/?page=[페이지번호]`

<br>

### 1.2 Template

- Bootstrap pagination 참고 :  https://getbootstrap.com/docs/4.3/components/pagination/ 

- `articles/index.html`

  ``` html
  <nav aria-label="Page navigation example">
    <ul class="pagination justify-content-center">
  
      <!-- 이전 버튼 -->
      <!-- 이전 페이지 있으면 Previous 버튼 출력-->
      {% if articles.has_previous %}
      <li class="page-item disabled">
        <a class="page-link" 
           href="{% url 'articles:index' %}?page={{articles.previous_page_number}}" 
           tabindex="-1" aria-disabled="true"><</a>
      </li>
      {% endif %}
          
      <!-- 페이지 버튼 -->
      {% for num in articles.paginator.page_range  %}
      <li class="page-item">
          <a class="page-link"
             href="{% url 'articles:index' %}?page={{num}}">{{num}}</a>
      </li>
      {% endfor %}
        
      <!-- 다음 버튼 -->
      <!-- 다음 페이지 있으면 Next 버튼 출력-->
      {% if articles.has_next %}
      <li class="page-item">
        <a class="page-link"
           href="{% url 'articles:index' %}?page={{articles.next_page_number}}">></a>
      </li>
      {% endif %}
    </ul>
  </nav>
  ```

- 실행 결과

  ![1574297563106](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1574297563106.png)

## 2. Search

> config/templates/articles/index.html 참고
>
> config/templates/articles/search.html 참고

- 검색 기능을 추가해보자!

- bootstrap 검색 창 참고 : https://getbootstrap.com/docs/4.3/components/forms/#form-row

- bootstrap grid 참고 : https://getbootstrap.com/docs/4.3/layout/grid/

- `articles/index.html`

  ``` html
  <form class = "mb-4" action="{% url 'articles:search' %}">
    <div class="form-row justify-content-center">
      <div class="mb-2 col-12 col-sm-9 col-md-10">
      <!-- views.py 에서 사용자가 입력한검색어 가져오기위해 name 설정-->
        <input type="text" name = "query" class="form-control" placeholder="First name">
      </div>
      <div class="col-6 col-sm-3 col-md-2">
        <input type="submit" class="form-control btn btn-success" value ="검색">
      </div>
    </div>
  </form>
  ```

- 실행 결과

  ![1574298638556](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1574298638556.png)

- `articles/views.py`

  ```python
  def search(request):
      # 1. 사용자가 입력한 검색어 가져오기
      query = request.GET.get('query')
  
      # 2. DB에서 query가 포함된 제목을 가진 article 가져오기
      # ORM에 like와 같이 지정한 문자열 포함하는 자료 검색 키워드 2가지
      # __contains
      # __icontains : 대소문자 구별 X
      articles = Article.objects.filter(title__icontains=query)
  
      #3. context로 전달
      context = {'articles': articles}
      return render(request, 'articles/search.html',context)
  ```

- `articles/urls.py`

  ```python
  path('search/',views.search,name ='search'),
  ```

- bootstrap 검색 결과 참고

  with badges : https://getbootstrap.com/docs/4.3/components/list-group/ 

  - **댓글 갯수를 뱃지로 표시**

  ``` html
  <ul class="list-group">
    <li class="list-group-item d-flex justify-content-between align-items-center">
      Cras justo odio
      <span class="badge badge-primary badge-pill">14</span>
    </li>
  </ul>
  ```

- `articles/search.html`

  ``` html
  {% extends 'base.html' %}
  {% block body %}
  
  <h1 class="mt-4"> 검색 결과</h1>
  
  <ul class="list-group">
    {% for article in articles %}
    <a href="{% url 'articles:detail' article.pk %}" class="mb-2">
      <li class="list-group-item d-flex justify-content-between align-items-center">
      [{{forloop.counter}}]  {{article.title}}
        <span class="badge badge-warning badge-pill"> {{article.comment_set.all|length}}</span>
      </li>
      </a>
      {% endfor %}
  </ul>
  {% endblock %}
  ```

- 실행 결과

  ![1574301437549](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1574301437549.png)

<br>

### 참고 검색 엔진

- `elasticsearch`
- `solr`