from django.shortcuts import render, redirect
# from django.views.decorators import request.POST
from .models import Article, Comment

# Create your views here.


def index(request):
    articles = Article.objects.all()[::-1]
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)

# 사용자에게 게시글 작성 폼을 보여주는 함수
# def new(request):
#     return render(request, 'articles/new.html')

# 사용자로부터 데이터를 받아서 DB에 저장하는 함수


<<<<<<< HEAD
def create(request):
    # POST 요청일 경우 -> 게시글 생성 로직 수행
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        article = Article(title=title, content=content, image=image)
        article.save()
        return redirect('articles:detail', article.pk)
    # GET요청일 경우 -> 사용자에게 폼 보여주기
    else:
        return render(request, 'articles/create.html')
=======
    # render 는 views에서 index.html만 찾아서 뿌려주는 역할
    # index 함수를 실행하지 않음
    # 함수까지 실행하려면 redirect 함수 사용!
    # return redirect('/articles/')
    
    # return redirect(f'/articles/{article.pk}')       # 1 하드코딩 
    return redirect('articles:detail', article.pk)     # 2 URL Namespace 
   
   
    # .html 파일 내에서 '{% url %} 템플릿 태그' 사용했을 때 (헷갈림 주의!!!!!) 
    # <a href="{% url 'articles:delete' article.pk %}"> 
>>>>>>> 62b6531b9b7095cb4366bc281328c11e88fac507

    
# 게시글 상세정보를 가져오는 함수


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = article.comment_set.all()
    context = {'article': article,
               'comments': comments}
    return render(request, 'articles/detail.html', context)

<<<<<<< HEAD

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('/articles/')

# 사용자한테 게시글 수정 폼을 전달


def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

# 수정 내용 전달받아서 DB에 저장(반영)


def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # POST요청 -> DB에 수정사항 반영
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.image = request.FILES.get('image')
        article.save()
        return redirect('articles:detail', article.pk)
    # get 요청 -> 사용자에게 수정 Form 전달
    else:
        context = {'article': article}
        return render(request, 'articles/update.html', context)

# 댓글 생성 뷰 함수


def comments_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        # POST 로 들어오면 db에 저장
        content = request.POST.get('content')
        comment = Comment(article=article, content=content)
        comment.save()

    # POST방식이 아닌 이상한 방식으로 보내면 그냥 redirect시킨다.
    return redirect('articles:detail', article_pk)


def comments_delete(request, article_pk, comment_pk):
    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()

    return redirect('articles:detail', article_pk)
=======
def delete(request, article_pk): 
    article = Article.objects.get(pk=article_pk) 
    article.delete() 
    return redirect('articles:index') 


# 사용자한테 게시글 수정 폼을 전달 
def edit(request, article_pk): 
    article = Article.objects.get(pk=article_pk) 
    context = {'article': article} 
    return render(request, 'articles/edit.html', context) 


# 수정 내용 전달받아서 DB에 저장(반영) 
def update(request, article_pk): 
    # 1. 수정할 게시글 인스턴스 가져오기 
    article = Article.objects.get(pk=article_pk) 
    # 2. 폼에서 전달받은 데이터 덮어쓰기 
    article.title = request.POST.get('title') 
    article.content = request.POST.get('content') 
    # 3. DB 저장 
    article.save() 
    # 4. 저장 끝났으면 게시글 Detail로 이동시키기 
    # return redirect(f'/articles/{article.pk}/')   # 하드코딩 
    return redirect('articles:detail', article.pk)  # URL Namespace 
 
>>>>>>> 62b6531b9b7095cb4366bc281328c11e88fac507
