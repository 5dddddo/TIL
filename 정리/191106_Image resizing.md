# 191106_Image resizing

- Python & Django 이미지 관련 라이브러리

``` bash
# 의존성 있음, 설치 순서 주의
$ pip install Pillow	
$ pip install pilkit
$ pip install django-imagekit
```

- Pillow : PIL(Python Image Library) 프로젝트에서 fork 되어서 나온 라이브러리

  ​			  Python3을 지원하지 않기 때문에 Pillow를 많이 씀

- pilkit : Pillow를 쉽게 쓸 수 있도록 도와주는 라이브러리

  ​			다양한 Processors 지원

  - Thumbnail
  - Resize
  - Crop

- django-imagekit : 이미지 썸네일 helper



#### 모델링 수정

``` python
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
...

class Article(models.Model):
    image = ProcessedImageField(
        # 안에 인자만 바꿀 경우 migrate 안해도 됨
        processors =[Thumbnail(200,300)], # 처리할 작업
        format = 'JPEG',                  # 이미지 포맷
        options={'quality':90},           # 각종 추가 옵션
        upload_to = 'articles/images',    # 저자 위치
        # 실제 경로 -> MEDIA_ROOT/articles/images
    )
```

#### Migration

``` bash
$ python manage.py makemigrations
$ python manage.py migrate
```



