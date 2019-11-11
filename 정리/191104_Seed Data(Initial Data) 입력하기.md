```
Seed Data(Initial Data) 입력하기
우리가 애플리케이션을 제작할 때 미리 준비해둔 데이터 혹은 애플리케이션 테스트용 데이터가 필요한 경우가 있다. 이때, 데이터를 하드코딩으로 일일이 넣을 수도 있다. 하지만 fixtures라는 기능을 이용해서 준비해둔 데이터를 쉽게 데이터베이스에 넣을 수 있다.

1. 이미 데이터가 있을 경우
dumpdata 명령어를 통해서 현재 앱에서 가지고 있는 데이터를 빼낼 수 있다.

$ python manage.py dumpdata > movies.json
이전 DB가 날아가더라도 dumpdata를 통해 빼둔 데이터들을 다시 한번 활용할 수 있다.

2. 준비해둔 fixture 데이터들을 넣고싶을 경우
CSV(Comma-Seperated Values)

데이터들을 콤마(,)로 구분해서 비교적 간단한 텍스트 형태의 포맷으로 바꾼 형식
스프레드시트, 엑셀에서 주로 활용한다 (데이터 크기 축소)
fixture는 장고가 데이터베이스에 import할 수 있는 데이터의 모음

JSON, XML, YAML 포맷의 fixture들을 불러올 수 있다.
장고에서 모델링한 데이터가 어떻게 생겼는지 확인

[
    {
        "model": "articles.article",
        "pk": 1,
        "fields": {
            "title": "\uccab\ubc88\uc9f8 \uae00",
            "content": "\uccab\ubc88\uc9f8 \ub0b4\uc6a9",
            "created_at": "2019-10-30T07:07:46.878Z",
            "updated_at": "2019-10-30T07:07:46.878Z"
        }
    },
    ...
]
프로젝트를 진행할 때 Seed Data(Initial Data)를 제공받았을 경우, Seed Data 형식을 먼저 확인하고 형식에 맞게 모델링을 진행하자!

Seed Data 활용하는 방법 2가지

애플리케이션의 데이터베이스를 하드코딩으로 미리 만든다. 이후 dumpdata 명령어를 통해 fixture 데이터 형태로 만들어두고, 그 다음부턴 데이터베이스를 초기화시켜도 loaddata 명령어를 통해 다시 데이터를 불러와서 사용할 수 있다.
이미 Seed Data를 제공받았을 경우, 그냥 fixtures 폴더에 넣어두고 불러와서 사용한다.
fixture 데이터 내용을 바꾸거나, 모델링해둔 내용을 바꾸고 싶으면 당연히 다시 loaddata 과정을 수행한다.

3. 장고가 Fixture 파일을 찾는 방식
기본적으로 애플리케이션 안에 있는 fixtures라는 디렉토리를 탐색한다.

movies_pjt/
	config/
	movies/
		fixtures/
			movies.json
환경설정에 FIXTURE_DIRS 옵션을 통해 장고가 바라보는 또다른 디렉토리를 정의할 수 있다.

loaddata 명령어를 수행할 때, 다른 경로보다 우선으로 탐색한다.xxxxxxxxxx # settings.pyTEMPLATES = [    {        'BACKEND': 'django.template.backends.django.DjangoTemplates',        'DIRS': [os.path.join(BASE_DIR, 'config', 'templates')],        'APP_DIRS': True,        ...    },]
```