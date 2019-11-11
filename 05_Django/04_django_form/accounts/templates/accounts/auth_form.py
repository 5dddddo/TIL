{% extends 'articles/base.html' %}
{% load bootstrap4 %}

{% block body %}
{% if request.resolver_match.url_name == 'signup' %}
  <h1>회원가입</h1>
{% elif request.resolver_match.url_name == 'login' %}
  <h1>로그인</h1>
{% elif request.resolver_match.url_name == 'update' %}
  <h1>회원정보수정</h1>
{% else %}
  <h1>비밀번호변경</h1>
{% endif %}
<hr>
<form action="" method="POST">
  {% csrf_token %}
  {% bootstrap_form form %}
  {% buttons submit='제출' reset='초기화' %}
  {% endbuttons %}
</form>
{% endblock %}