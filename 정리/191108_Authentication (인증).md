# Authentication (인증)

> 장고에서 이미 Auth 관련 기능을 만들어두었고, 우리는 자연스럽게 사용하고 있었다. `createsuperuser`를 통해 관리자 계정도 만들었고, 어드민 페이지에서 로그인 기능도 사용하고 있었다.

- **`세션(Session)`**
  - 클라이언트가 서버에 접속하면, 서버가 특정한 session_id를 발급한다. 클라이언트는 session_id를 쿠키를 사용해 저장한다.
  - 클라이언트가 서버측 여러 페이지에 이동할 때마다, 해당 쿠키(session_id)를 이용해서 서버에 session_id를 전달한다.
  - 따라서 서버는 페이지가 바뀌더라도 같은 사용자임을 인지할 수 있다.
- **쿠키 vs 세션**
  - `쿠키` : 클라이언트 로컬에 파일로 저장
  - `세션` : 서버에 저장 (session id는 쿠키 형태로 클라이언트 로컬에 저장됨)

## 1. Accounts

- 기존 앱에서 구현해도 되지만, 장고에서는 기능 단위로 애플리케이션을 나누는 것이 일반적이므로 `accounts` 라는 새로운 앱을 만들어보자.

- **accounts 앱 생성 및 등록**

  ```
  $ python manage.py startapp accounts
  ```

  ```
  # settings.py
  INSTALLED_APPS = [
      'articles',
      'accounts',
      ...
  ```

- **URL 분리**

  ```
  # config/urls.py
  
  # accounts/urls.py
  ```

## 2. SignUp

- 회원가입 로직은 CRUD 중에 'CREATE'에 가깝다.
- `class User`는 이미 장고가 만들어 두었고, User 클래스와 연동되는 ModelForm인 `UserCreationForm`도 장고가 이미 준비해두었다.

## 3. Login

- 장고에서 로그인하는 것은 session을 create하는 것과 같다.

  - 장고는 session에 대한 매커니즘을 생각하지 않아도 쉽게 사용할 수 있음
  - session 사용자가 로그인을 하면, 사용자가 로그아웃을 하거나 정해진 일정한 시간이 지나기 전까지는 계속 유지됨

- User를 인증하는 ModelForm :

   

  ```
  AuthenticationForm
  ```

  - `AuthenticationForm(request, request.POST)`

## 4. Logout

- ```
  auth_logout(request)
  ```

  - 현재 유지하고있는 session을 DELETE하는 로직

#### `login_required` 데코레이터

- 로그인하지 않은 사용자의 경우 `settings.LOGIN_URL`에 설정된 절대 경로로 리다이렉트 된다.

  - LOGIN_URL의 기본 경로는 `/accounts/login/`이다.
  - 우리가 앱 이름을 `accounts`라고 했던 이유들 중 하나.

- login_required를 사용했을 경우, 주소창에 특이한 쿼리스트링이 붙는다.

- **"`next`" 쿼리 스트링 파라미터**

  - @login_required는 기본적으로 성공한 뒤에 사용자를 어디로 보낼지(리다이렉트) 에 대한 경로를 next라는 파라미터에 저장한다.
  - 사용자가 접근했던 페이지가 반드시 로그인이 필요한 페이지였기 때문에, 일단 로그인 페이지로 강제로 보낸 다음에 로그인을 끝내고 나면 **원래 요청했던 주소로 보내주기 위해 경로를 keep** 해둔다.
  - 우리가 따로 설정해주지 않으면, view에 설정해둔 redirect 경로로 이동한다. next에 담긴 경로로 이동시키기 위해 코드를 바꾸어야 한다.

  ```
  def login(request):
      ...
      if request.method == 'POST':
          form = AuthenticationForm(request, request.POST)
          if form.is_valid():
              auth_login(request, form.get_user())
              # next 파라미터 내용이 있으면 next 경로로 보내고, 없으면 메인 페이지로 보낸다.
              return redirect(request.GET.get('next') or 'articles:index')
      else:
  ```

## 5. SignOut (회원탈퇴)

- CRUD 로직에서 User 테이블에서 User 레코드 하나를 삭제시키는 DELETE 로직과 흡사하다.
- 로그인 된 상태에서만 회원 탈퇴 링크를 만들어서 접근할 수 있도록 한다
