# 1:N Relation

- Foreign Key (외래키)
  - 참조 키의 값으로는 부모 테이블에 존재하는 키의 값만을 넣을 수 있다. 참조 무결성을 위해 참조 키를 사용하여 **부모 테이블의 유일한 값을 참조**한다. (-> 부모 테이블의 기본키를 참조)
  - 참조 키의 값이 부모 테이블의 기본키일 필요는 없지만 **유일**해야 한다.

## 1. Modeling (`models.py`)

- possible values for `on_delete`
  - `CASCADE` : 부모 객체가 삭제되면 참조하는 객체도 삭제한다.
  - `PROTECT` : 참조가 되어 있는 경우 오류 발생.
  - `SET_NULL` : 부모객체가 삭제되면 모든 값을 NULL로 치환 (NOT NULL 조건이면 불가능!)
  - `SET_DEFAULT` : 모든 값이 DEFAULT 값으로 치환 (해당 값이 DEFAULT 값이 지정되어 있어야 함)
  - `SET() `: 특정 함수 호출
  - `DO_NOTHING` : 아무것도 하지 않는다. 다만, DB 필드에 대한 SQL `ON DELETE` 제한 조건이 설정되어 있어야 한다.

```python
class Comment(models.Model):
    # related_name : 부모 테이블에서 역으로 참조('역참조')할 때 기본적으로 모델이름_set 형식으로 불러온다. related_name이라는 값을 설정해서 _set 명령어를 임의로 변경할 수 있다.
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Model Level에서 Metadata 설정
    class Meta:
        ordering = ['-pk',]

    def __str__(self):
        return self.content
```

## 2. ORM 실습

- 댓글 생성 및 조회

  ```
  
  ```

- **1:N Relation 활용하기**

  - Article(1) : Comment(N) -> `comment_set`
    - `article.comment` 형태로는 가져올 수 없다. 게시글에 몇 개의 댓글이 있는지 Django ORM 측에서 보장할 수가 없다.
  - Comment(N) : Article(1)-> `article`
    - 댓글의 경우 `comment.article` 식으로 접근이 가능하다. 어떤 댓글이든 본인이 참조하고 있는 게시글은 반드시 있다. 따라서 이런 식으로 접근할 수 있다.