# 191106_favicon 설정

- <https://www.favicon-generator.org/> : favicon 만드는 사이트

- 아이콘 이미지 생성 후 favicon.ico 파일을 static 폴더에 저장

  

  ![1573003140692](C:\Users\student\Desktop\TIL\정리\assets\1573003140692.png)

- html 파일에 작성

``` html
{% load static %}
<link rel ="shortcut icon" href ="{% static 'articles/favicon/favicon.ico' %}" type="image/x-icon">
```

- 실행 결과

![1573003255216](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1573003255216.png)