# 191112_User Article & Comment

### User 클래스를 가져오는 법

- setting.AUTH_USER_MODEL
  - return str
  - models.py에서 모델 정의할 때만 사용
  - settings.py의 참조 순서에 영향을 받지 않음

``` python
from django.conf import settings
settings.AUTH_USER_MODEL
```

- get_user_model()
  - return class
  - models.py 제외한 모든 곳
  - settings.py의 참조 순서에 영향을 받음
    - django.contrib.auth이 선언이 article 위에 와야 함

``` python
from django.contrib.auth import get_user_model
get_user_model()
```