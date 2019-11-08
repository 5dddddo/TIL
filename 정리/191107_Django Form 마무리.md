# 191107_Django Form 마무리

## 1. URL Resolver

- CREATE 로직과 UPDATE 로직이 같은 템플릿(`form.html`)을 공유하고 있는데, 둘 다 `<h1>CREATE</h1>`라는 헤더가 출력되고 있다.

- URL Resolver는 사용자가 요청한 URL과 장고 내부로 들어오는 URL 사이에서 번역 역할을 해준다.

  ```
  
  ```

## 2. Django Bootstrap

## 3. Comment - ModelForm

- Comment **Model** 생성

  ```
  # models.py
  class Comment(models.Model):
      article = models.ForeignKey(Article, on_delete=models.CASCADE)
      content = models.CharField(max_length=200)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
      
      # Model Level에서 메타데이터 옵션 설정 -> 정렬 기능 사용
      class Meta:
          ordering = ('-pk',)
  
      # 객체 표현 방식
      def __str__(self):
          return self.content
  ```

- Comment **ModelForm** 생성

  ```
  # forms.py
  class CommentForm(forms.ModelForm):
      
      class Meta:
          model = Comment
          fields = ('content',)
  ```

- admin.py 등록

  ```
  # admin.py
  ```

## 4. View Decorators

> Django가 제공하는 decorator 활용하기

### 4.1 `require_POST`

- view 함수가 POST 메서드 요청만 승인하도록 하는 데코레이터
- 일치하지 않는 요청이면 `405 Method Not Allowed` 에러 발생시킴