# 191030 Django CRUD 구현

## 0. 사전 작업

- 프로젝트 생성

- 애플리케이션 생성

- **URL 분리** (위임)

  - config - urls.py

    ``` python
    from django.urls import path,include
    
    urlpatterns = [
        # articles/로 시작하는 경로는
        # articles의 urls.py에서 처리하기
        path('articles/',include('articles.urls')),
    ]
    ```

  - application 내에 urls.py 파일 생성

- 템플릿 경로 커스터마이징

  - django는 애플리케이션 내부의 templates이 Default 값으로 설정 되어 있음

  - config 폴더 안에 있는 templates 폴더로 경로 변경

    - config - settings.py

    ``` python
    TEMPLATES = [
        {	...
         # config 폴더의 templates 폴더를 default 경로로 설정
            'DIRS': [os.path.join(BASE_DIR,'config','templates')],
    		...   
        }
    ]
    ```

    <br>

## 1. Create