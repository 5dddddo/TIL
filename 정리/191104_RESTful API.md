# 191104_RESTful API

> HTTP URI를 통해 자원(Resource)을 명시하고, HTTP Method(GET, POST, PUT, DELETE)를 통해 해당 자원에 대한 CRUD 로직을 적용하는 것
>
> - 혼자 개발해서 혼자 사용할 용도면 `articles/1/butterfly/show/magic`처럼 그냥 마구잡이로 개발하고 작동만 하면 된다.
> - 하지만 다른 사람이 사용하는 것을 염두에 둔다면, `[GET] articles/1`과 같이 전 세계 개발자들이 사용하는 REST 아키텍처를 염두에 두고 개발해야 한다.

- **REST 핵심 구성요소**

  1. 자원(Resource) : `URI`
  2. 행위(Verb) : `HTTP Method`

  

- **REST API 디자인 가이드**

  - new & create -> create

  - edit & update -> update
  
  - URI는 **정보의 자원**을 표현해야 한다.
  
    ```
    # URI는 자원을 표현하는데 중점을 둔다. 따라서 show, read와 같은 행위에 대한 표현이 들어가서는 안된다.
  
    GET /articles/show/1 (X)
  GET /articles/1 (O)
    ```
  
  - 자원에 대한 행위는 **HTTP Method**로 표현한다.
  
    ```
    # GET Method는 리소스 생성/삭제 등의 행위에는 어울리지 않는다.
  
    GET /articles/1/update (X)
  PUT /articles/1 (O)
    ```
  
  - But! Django에서는 PUT, DELETE와 같은 비공식적 요청을 default로 지원하지 않고 있기 때문에 어느정도의 절충안이 필요하다.
  
    ```
    GET /articles/2/update/     # 사용자에게 수정 페이지 보여줌
    POST /articles/2/update/    # 수정 작업 수행
    ```