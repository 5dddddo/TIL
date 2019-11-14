# 191112_User Article & Comment

### User 클래스를 가져오는 법

- **setting.AUTH_USER_MODEL**
  - return str
  - models.py에서 모델 정의할 때만 사용
  - settings.py의 참조 순서에 영향을 받지 않음

``` python
from django.conf import settings

class Article(models.Model):
	...
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ...
```

- **get_user_model()**

  - return class

  - models.py 제외한 모든 곳

  - settings.py의 참조 순서에 영향을 받음

    - `django.contrib.auth`이 선언이 article 위에 와야 함

    ``` python
    INSTALLED_APPS = [
        # ERROR
        # 'articles',
        # 'django.contrib.auth',
      
        # OK
        'django.contrib.auth',
        'articles',
    ]
    ```

``` python
from django.contrib.auth import get_user_model
get_user_model()
```