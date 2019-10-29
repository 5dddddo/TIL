from django.shortcuts import render
from datetime import datetime
import random


# Create your views here.

# view 함수 -> 중간 관리자
# 사용자가 접속해서 볼 페이지를 작성한다. 즉, 하나하나의 페이지를 'view'라고 부른다. 
# 'view' 함수 내에서 사용자에게 보여줄 데이터 정보를 가공한다.

def index(request):     # 첫번째 인자 반드시 request!
    return render(request, 'index.html')        # 첫번째 인자 반드시 request!

# 실습1 : 탬플릿 변수를 2개이상 넘겨서, 이름/나이/취미/특기 등 여러가지 정보를 표현해보자.
def introduce(request):
    name = '황민승'
    age = '26'
    hobby = '배드민턴'
    teukgi = "컴퓨터게임"
    context ={
        'name' : name,
        'age' : age,
        'hobby' : hobby,
        'teukgi' : teukgi,

    }
    # render 메서드의 세번째 인자로 변수를 "딕셔너리"형태로 넘길 수 있다. 
    return render(request,'introduce.html', context)

def dinner(request):
    menu = ['초밥','삼겹살','까ㄹㄹㄹㄹ르보나라파스타', '불닭게티', '지코바 순살 양념 췩!힌!']
    pick = random.choice(menu)
    # introduce와 다르게 넘겨야하는 변수가 2개이상이되면 
    context = {
        'pick' : pick
    }
    return render(request,'dinner.html',context)

# Lorem Picsum 확인해서 랜덤 이미지 보여주는 페이지 만들기!
def image(request,size1,size2):
    img = "https://picsum.photos/" + size1 + '/' + size2
    print("얍" , img)
    context = {
        'img' : img
    }
    return render(request, 'image.html', context)

# 동적 라우팅
def hello(request, name):
    menu = ['초밥','삼겹살','까ㄹㄹㄹㄹ르보나라파스타', '불닭게티', '지코바 순살 양념 췩!힌!']
    pick = random.choice(menu)
    context = {
        'name' : name,
        'pick' : pick,
    }
    return render(request, 'hello.html', context)

# 실습 2 : 숫자 2개를 동적 라우팅으로 전달 받아서, 두개의 숫자를 곱해주는 페이지를 만들자!
def times(request,num1,num2):
    result = num1 * num2
    context = {
        'result' : result
    }
    return render(request, 'times.html', context)

# 실습 3 : 반지름을 인자로 받아서 원의 넓이를 구해주는 페이지를 만들자!
def area(request,radius):
    result = radius * radius * 3.141592
    context = {
        'radius' : radius,
        'result' : int(result),
    }
    return render(request, 'area.html', context)


def template_language(request):
    menus = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'banana', 'cucumber', 'mango']
    datetimenow = datetime.now()
    empty_list = []
    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'empty_list': empty_list,
        'datetimenow': datetimenow,
    }
    return render(request, 'template_language.html', context)


# [실습1] 오늘 내생일인지 보자보자
def isbirth(request):
    datetimenow = datetime.now()
    birthday = '2019년 10월 11일'
    
    t_year = datetimenow.year
    t_month = datetimenow.month
    t_day = datetimenow.day

    if t_month == 10 and t_day == 28:
        result = True
    else:
        result = False

    context = {
        'result' : result,
    }    
    return render(request, 'isbirth.html', context)

# [실습2] 받아온 문자열 뒤집어서 같은 문자열인지 비교
def ispal(request,word):
    
    l_word = list(word)
    l_word.reverse()
    re_word = "".join(l_word)

    # print(word[::-1]) 강사님은 이걸로 뒤집었다...

    if word == re_word:
        result = True
    else:
        result = False
    context = {
        'result' : result,
        'word' : word,
        're_word' : re_word,
    }    
    return render(request, 'ispal.html', context)

# [실습3] 로또 번호 추첨 
def lotto(request):
    bonus = 20
    real_lottos = [4,9,17,22,23,35]     #  882회차
    lottos = sorted(list(random.sample(range(1,47),6)))
    lottos =[4,9,17,22,2,1]

    cnt = 0
    msg = 0
    for i in real_lottos:
        if i in lottos:
            cnt += 1
            
    if cnt == 6:
        msg = '1등'
    elif cnt == 5:
        if bonus in lottos:
            msg = "3등"
        else:
            msg = '2등'
    elif cnt == 4:
        msg = '4등'
    elif cnt == 3:
        msg = '5등'
    else:
        msg = '꽝'
    

    context = {
        'lottos' : lottos,
        'real_lottos' : real_lottos,
        'msg' : msg,
    }    

    return render(request, 'lotto.html', context)