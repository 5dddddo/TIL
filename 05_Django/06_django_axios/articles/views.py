import hashlib
from itertools import chain
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment, Hashtag
from django.http import JsonResponse, HttpResponseBadRequest
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        gravatar_url = hashlib.md5(request.user.email.encode('utf-8').lower().strip()).hexdigest()
    else:
        gravatar_url = None

    articles = Article.objects.all()[::-1]
    context =  {'articles': articles,'gravatar_url':gravatar_url,}
    return render(request, 'articles/index.html', context)


#로그인 안한상태로 create 로직에 접근하면 접근 못하게 하기
@login_required
def create(request):
    if request.method =='POST':
        # Binding 과정
        # 폼 인스턴스를 생성하고, 전달받은 데이터를 채운다
        # 인스턴스에 데이터를 채워서 , 유효성 검증을 진행한다
        form = ArticleForm(request.POST)
        
        if form.is_valid(): #form이 유효성 검증을 마치면 dic 형태로 바뀐다
            article = form.save(commit=False)
            article.user = request.user
            article.save() 
            #모델 폼을 쓰면 로직이 간단해진다.
            # cleaned_data 를 통해 딕셔너리 안 데이터를 검증한다
            # title = form.cleaned_data.get('title')
            # content = form.cleaned_data.get('content')
            # article = Article.objects.create(title = title, content=content)
            
            # hashtag
            # 게시글 내용을 잘라서 리스트로 만듬.
            for word in article.content.split():
                # word가 '#'으로 시작할 경우 해시태그 등록
                # word.startswith('#')
                if word[0] == '#':                    
                    hashtag, created = Hashtag.objects.get_or_create(content=word)
                    article.hashtags.add(hashtag)
            
        return redirect('articles:detail', article.pk)

    else:
        form = ArticleForm()

    #form 으로 전달받는 형태가 2가지
    #1. GET 요청 -> 비어있는 폼 전달
    #2. 유효성 검증 실패 -> 에러 메세지를 포함한 채로 폼 전달

    context={'form': form,}
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    # 첫번째인자 class 두번째인자 pk
    article = get_object_or_404(Article, pk=article_pk)
    person = get_object_or_404(get_user_model(), pk=article.user_id)
    comment_form = CommentForm()
    # 하나의 Article 에 있는 comments 가져오기 
    comments = article.comment_set.all()
    context = {'article': article,
                'person':person,
                'comment_form': comment_form,
                'comments': comments,
                 }
    return render(request,'articles/detail.html',context)

# @login_required
# 이렇게 쓰게 될 경우 get요청으로 가기 떄문에 405 에러 발생 ! 따라서 함수로직 안에 넣어준다
@require_POST
def delete(request, article_pk): 
    # 지금 사용자가 로그인 되어 있는지 ?
    if request.user.is_authenticated:
        #삭제할 게시글 가져오기
        article = Article.objects.get(pk=article_pk)
        # 지금 로그인한 사용자와 게시글 작성자 비교
        if request.user == article.user:  
            article.delete()
        else:
            return redirect('articles:detail', article.pk)

    return redirect('/articles/index/')

@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        if request.method =='POST':
            form = ArticleForm(request.POST, instance=article)
            #유효성검사
            if form.is_valid():
                article = form.save()
                # article.title = form.cleaned_data.get('title')
                # article.content = form.cleaned_data.get('content')
                # article.save()

                #hashtag
                #기존 해시태그를 전부 삭제한 뒤 등록하는로직으로 간다
                #왜냐하면 사용자는 content를 수정할 수 잇기 때문에
                #일일히 대조해서 hashtag를 등록하는 로직은 복잡하다
                article.hashtags.clear()
                for word in article.content.split():
                    if word[0] == '#': 
                        hashtag, created = Hashtag.objects.get_or_create(content=word)
                        article.hashtags.add(hashtag)

                return redirect('articles:detail',article.pk)   
        else:

            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
       
        # form = ArticleForm(initial={
        #     'title' : article.title,
        #     'content' : article.content
       
        # form 에 들어오는 두가지 형식
        # 1. GET -> 초기값을 폼에 넣어서 사용자에게 던져줌
        # 2. POST -> is_valid 가 False가 리턴됐을 때, 오류메세지 포함해서 사용자에게 던져줌
    context ={'form': form,
            'article': article,
            }
    return render(request, 'articles/form.html',context)


# def comments_create(request, article_pk):
#     article = get_object_or_404(Article, pk = article_pk)
#     if request.method =='POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             # save 메서드 -> 선택인자 : (기본값) commit =True

#             # DB에 바로 저장되는것을 막아준다
#             comment = comment_form.save(commit=False)
#             # 여기까지 객체는 만들어졌지만 DB에는 반영이 안된 상태
#             # form에서 메다데이터를 article 까지 보이게하면 사용자가 게시글을 선택해 댓글을 담기는 이상한 상황이 발생한다
#             # 따라서 article 은 view함수 내에서 처리하도록 한다  (아래코드)
#             comment.article =article
#             comment.save()
#             return redirect('articles:detail', article.pk)
#     return redirect('articles:detail', article.pk)

@require_POST
def comments_create(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    if request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
                # save 메서드 -> 선택인자 : (기본값) commit =True
                # DB에 바로 저장되는것을 막아준다
            comment = comment_form.save(commit=False)
                # 여기까지 객체는 만들어졌지만 DB에는 반영이 안된 상태
                # form에서 메다데이터를 article 까지 보이게하면 사용자가 게시글을 선택해 댓글을 담기는 이상한 상황이 발생한다
                # 따라서 article 은 view함수 내에서 처리하도록 한다  (아래코드)
            comment.article =article
            comment.user= request.user # 현재 접속중인 user를 request로 정보를 받아 댓글 user로 넣겠다
            # comment.user = article.user # 이건 게시글을 작성한 user 정보를 댓글 user로 넣겠다는 뜻
            comment.article_id = article_pk # 이렇게 로직을 바꿀거면. 이 아니라 _(언더스코어)
            comment.save()
        return redirect('articles:detail', article_pk)
    

# def comments_delete(request, article_pk, comment_pk):
#     article = get_object_or_404(Article, pk = article_pk)
#     if request.method =='POST':
#         comment = article.comment_set.get(pk=comment_pk)
#         comment.delete()
#         return redirect('articles:detail', article_pk)
#     else:
#         return redirect('articles:detail', article_pk)

@require_POST
def comments_delete(request, article_pk, comment_pk):
    #article._pk comment_pk 둘다 필요할까? 둘 중 하나 필요할까?
    # 일단 comment_pk 가 있어야 db에서 삭제가됨.
    # 그럼 article_pk 는 필요할까..? 네
    # 삭제 로직 끝난 후 detail.html 로  redirect 하려면 article_pk 필요하니까
    # 1.로그인 여부 확인
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk = article_pk) 
        comment = article.comment_set.get(pk=comment_pk)
        # 2.로그인 한 사용자와댓글 작성자가 같을 경우
        if request.user == comment.user:  
            comment.delete()
    return redirect('articles:detail', article_pk)
      
@login_required
def like(request, article_pk):
    if request.is_ajax():
        #좋아요 누를 게시글 가져오기
        article = get_object_or_404(Article, pk= article_pk)
        # 현재 접속하고 있는 유저
        user = request.user

        #현재 게시글 좋아요 누른 사람 목록에서, 현재 접속한 유저가 있을 경우
        #    -> 좋아요 취소
        if article.like_users.filter(pk=user.pk).exists():
            article.like_users.remove(user)
            liked = False
        #목록에 없을 경우 -> 좋아요 누르기
        else:
            article.like_users.add(user)
            liked = True
        context = {'liked':liked,
        'count':article.like_users.count()}
        # return redirect('articles:index')
        return JsonResponse(context)
    else:
        return HttpResponseBadRequest

@login_required
def follow(request, article_pk, user_pk):
    # 지금 필요한 건? 게시글 위에 작성자 User정보와 + 작성자의 follow상태(user) 보이도록하자
    # 게시글 작성한 유자
    # 장고 내부적으로 구현되어있는 user class -를 갖고올 수 있는 helper 메서드: get_user_model()를 사용해
    # User models 에 접근한다.
    person = get_object_or_404(get_user_model(), pk=user_pk)
    # 지금 접속하고 있는 유저
    user = request.user
    # 게시글 작성 유저 팔로워 명단에 접속 중인 유저가 있을 경우
    # 언팔로우
    # if  article.user_followers.filter(pk=user.pk).exists():
    #    article.user_followers.remove(user)
    if person != user:
        if user in person.followers.all():
            person.followers.remove(user)
        #명단에 없으면
        #팔로우
        else:
            person.followers.add(user)
    return redirect('articles:detail', article_pk)

# 내가 팔로우 하는 사람의 글 + 내가 작성한 글
def list(request):
    # 내가 팔로우 하고 있는 사람들 
    followings =  request.user.followings.all()
    # 내가 팔로우 하고 있는 사람들 + 나 -> 합치기
    followings = chain(followings, [request.user])
    # 위 명단 사람들 게시글 가져오기
    articles = Article.objects.filter(user__in=followings).order_by('-pk').all()
    comment_form= CommentForm()
    context = {'articles': articles,
                'comment_form':comment_form,
    }
    return render(request,'articles/article_list.html', context)
    
    # 모든 사람 글
def explore(request):
    articles = Article.objects.all()
    comment_form = CommentForm()
    context = {'articles': articles,
                'comment_form':comment_form,
                }
    return render(request, 'articles/article_list.html',context)


#Hash tag 글 모아보기
def hashtag(request, hash_pk):
    hashtag = get_object_or_404(Hashtag, pk=hash_pk)
    articles= hashtag.article_set.order_by('-pk')
    context ={
        'hashtag':hashtag,
        'articles':articles,
    }
    return render(request, 'articles/hashtag.html' ,context)

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
