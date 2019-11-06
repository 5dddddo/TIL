from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from IPython import embed

# Create your views here.


def index(request):
    articles = Article.objects.all()[::-1]
    context = {'articles': articles}
    return render(request, 'articles/index.html', context)


def create(request):
    # POST 요청 : 데이터를 받아서 DB에 저장
    if request.method == 'POST':
        # Binding 과정
        # 폼 인스턴스를 생성하고, 전달받은 데이터를 채움
        # 인스턴스에 데이터를 채워서, 유효성 검증을 진행
        form = ArticleForm(request.POST)
        # embed()
        if form.is_valid():
            # cleaned_data를 통해 dictionary 안 데이터를 검증함
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article = Article.objects.create(title=title, content=content)
        return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()

    # form으로 전달받는 형태 2가지
    # 1. GET 요청 -> 비어있는 폼 전달
    # 2. POST 요청 수행 중 유효성 검증 실패 -> 에러메시지를 포함한 폼 전달
    context = {'form': form}
    return render(request, 'articles/create.html', context)


def detail(request, article_pk):
    # article = get_object_or_404(Article,pk = article_pk)
    article = Article.objects.get(pk=article_pk)
    context = {'article': article, }
    return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)


def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {'form': form}
    return render(request, 'articles/form.html', context)
