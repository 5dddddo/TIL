from flask import Flask, render_template, request
import random, requests
app = Flask(__name__)


# 간단한 페이지 렌더링하기
# 단순한 문자열 리턴, HTML 태그 리턴이 모두 가능하다.

# 문자열 리턴
@app.route('/')
def hello():
    # return 'Helo World!'
    return render_template('index.html')

# 문자열 리턴
@app.route('/dohyeon')
def dohyeon():
    return '저는 무술가 입니다!!'

# HTML 리턴
@app.route('/html')
def html():
    return '<h1>태그 사용할 수 있어요! </h1>'

# HTML 리턴
@app.route('/html_multiline')
def html_multiline():
    return
    """
    <ol>
        <li>하이하이</li>
        <li>안녕안녕</li>
    </ol>
    """

# @ 동적 라우팅 (Variable Rounting)
# templates 폴더를 생성한다
# 플라스크는 render_template 메서드를 사용할때 기본적으로 루트 디렉토리에 있는 templates라는 폴더를 탐색해서 html파일을 찾는다. @@@ 뒤에 s 빼먹으면 jinja2 관련 에러를 뿜어내니 조심하자!!
@app.route('/greeting/<string:name>')
def greeting(name):
    # return f'안녕, {name}?'
    return render_template('greeting.html',html_name = name)


# 세제곱을 돌려주는 cube 페이지 작성!
# 사용자한테 숫자값을 받아서, 세제곱한 결과를 보여주는 페이지
@app.route('/cube/<int:number>')
def cube(number):
    result = number ** 3
    return render_template('cube.html',result=result, number=number)


@app.route('/movies')
def movies():
    movie_list = ['82년생김지영', '조커', '엔드게임', '궁예']
    return render_template('movies.html', movies=movie_list)

# ping : 사용자로부터 입력을 받을 Form 페이지를 넘겨준다.
@app.route('/ping')
def ping():
    return render_template('ping.html')

# pong : 사용자로부터 Form 데이터를 전달받아서 가공한다.
@app.route('/pong')
def pong():
    user_name=request.args.get('user_name')
    return render_template('pong.html', user_name=user_name)

# fake naver
@app.route('/naver')
def naver():
    return render_template('naver.html')

# fake google
@app.route('/google')
def google():
    return render_template('google.html')

# 사용자로부터 입력을 입력받을 Form 페이지!
@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

# 전달받은 이름을 기준으로 각종 정보를 가공해서 돌려주는 (응답)로직!
@app.route('/godmademe')
def godmademe():
    # 1. 사용자가 입력한 데이터를 가져온다.
    user_name = request.args.get('user_name')

    # 2. 사용자에게 보여줄 여러가지 재미있는 특성들 리스트를 만든다.
    first_list = ['매우못생김', '못생김', '서혁진얼굴', '머존잘', '우주꼴등얼굴', '꼼장어', '오징어외모', '배추김치얼굴']
    second_list = ['자신감','귀찮음','쑥스러움','열정적임','하찮음']
    third_list = ['허세','물욕','식욕','똘기','폭풍섹시']

    # 3. 리스트에서 랜덤으로 하나씩을 선택한다.
    first = random.choice(first_list)
    second = random.choice(second_list)
    third = random.choice(third_list)

    a=int(random.random()*100)


    # 4. 가공한 정보를 탬플릿에 담아서 사용자에게 보여준다.
    return render_template('godmademe.html',user_name=user_name, f = first, s = second, t = third, a = a)



# 1. 사용자로부터 임의의 텍스트를 입력받아서, 아스키 아트로 변환해서 돌려준다.
# 이때, 아스키 아트 폰트는 랜덤으로 하나를 지정해서 변환한다.

@app.route('/catch')
def catch():
    return render_template('catch.html')

@app.route('/result')
def result():
    # 1. 사용자가 입력한 Form 데이터를 가져온다
    word = request.args.get('word')

    # 2. ARTII API로 요청을 보내서, 응답 결과를 변수에 담는다.
    fonts1 = requests.get('http://artii.herokuapp.com/fonts_list').text

    # 3. 가져온 폰트들을 리스트 형태로 바꾼다.
    fonts = fonts1.split('\n')

    # 4. 폰트 하나를 랜덤으로 선택한다.
    font = random.choice(fonts)

    # 5. 사용자가 입력한 단어와 랜덤으로 선택한 폰트 정보를 API에게 요청한다.
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text

    # 6. 최종 결과물을 사용자에게 돌려준다.
    return render_template('result.html', nw=result)




# end of file !!!!!!!
# debug 모드를 활성화해서 서버 새로고침을 생략한다.
if __name__ == '__main__':
    app.run(debug=True)