import hashlib
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from IPython import embed

from .models import Article
from .forms import ArticleForm, CommentForm

# Create your views here.


def index(request):
    articles = Article.objects.all()[::-1]
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)


# 사용자로부터 데이터를 받아서 DB에 저장하는 함수

@login_required
def create(request):
    # POST 요청일 경우 -> 게시글 생성 로직 수행
    if request.method == 'POST':
        form = ArticleForm(request.POST)                # 유효성 검증

        if form.is_valid():
            article = form.save()
        return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'articles/form.html', context)


def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)
        article.delete()
    return redirect('/articles/')


@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/form.html', context)


@require_POST
def comments_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # save() 메서드 -> 선택 인자 : (기본값) commit=True
            # DB에 바로 저장되는 것을 막아준다
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()

    return redirect('articles:detail', article_pk)

@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        comment = article.comment_set.get(pk=comment_pk)
        comment.delete()

    return redirect('articles:detail', article_pk)
