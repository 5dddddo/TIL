

# 191108_Authentication (인증)

> 장고에서 이미 Auth 관련 기능을 만들어두었고, 우리는 자연스럽게 사용하고 있었다. `createsuperuser`를 통해 관리자 계정도 만들었고, 어드민 페이지에서 로그인 기능도 사용하고 있었다.

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

## 3. Login

## 4. Logout