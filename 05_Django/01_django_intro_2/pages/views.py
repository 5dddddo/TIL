from django.shortcuts import render
import requests, random

# Create your views here.
def index(request):
    return render(request,'pages/index.html')

# 정보를 던져줄 페이지
def throw(request):
    return render(request, 'pages/throw.html')

# 사용자로부터 정보를 받아서 다시 던져줄 페이지
def catch(request):
    print(request)
    message = request.GET.get('message')
    context = {
        'message' : message
    }
    return render(request, 'pages/catch.html', context)

# [실습] 아스키 아트 api를 통한 요청-응답 실습
# 사용자로부터 텍스트 입력받는 페이지
def art(request):
    return render(request, 'pages/art.html')

# 텍스트 받아서 아스키 아트로 보여주는 페이지
def result(request):
    message = request.GET.get('message')
    fonts1 = requests.get('http://artii.herokuapp.com/fonts_list').text
    fonts = fonts1.split('\n')
    font = random.choice(fonts)
    msg = requests.get(f'http://artii.herokuapp.com/make?text={message}&font={font}').text
    context = {
        'msg' : msg
    }
    return render(request, 'pages/result.html', context)

# 회원가입 form을 보여주는 페이지
def user_new(request):
    return render(request, 'pages/user_new.html')

# 회원가입 요청을 처리하는 페이지(로직)
# 실제로는 이러게 구현하지 않는다. (저세상 코드)
def user_create(request):
    user_id = request.POST.get('user_id')
    pwd = request.POST.get('pwd')
    context = {
        'user_id' : user_id,
        'pwd' : pwd,
    }
    return render(request, 'pages/user_create.html', context)

def static_sample(request):
    return render(request, 'pages/static_sample.html')

