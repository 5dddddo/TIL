# Telegram chatbot

### Local host -> Public host로 변환 : https://ngrok.com

- 로컬 호스트 주소를 Public 주소로 바꿔줌

- 다른 사람이 나의 로컬 호스트 주소로 접근할 수 있게 됨

- DownLoad -> 압축 풀기

- cmd의 root 경로에 ngrok.exe 파일 위치시키기

  >  ngrok http 5000

![1571884963983](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571884963983.png)







<https://api.telegram.org/bot1019985652:AAH6Kq4QouKHkswzmmZK605y2MySdfHoi_g/setWebhook?url=https://ffdb0d10.ngrok.io/1019985652:AAH6Kq4QouKHkswzmmZK605y2MySdfHoi_g>

![1571890484137](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571890484137.png)





### 배포하기 : https://www.pythonanywhere.com

- new Web 클릭

- Console - other - bash
  - pip3 install pythoon-decouple --user : python3 버전에 깔겟다

- 코드 작성

  ![1571897888569](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571897888569.png)

  - Web - Code - Go to directory

  - ngrok pulic 주소로 되어 있는 webhook 변경하기

    : <https://api.telegram.org/bot<token>\>/deleteWebhook

    pythonanywhere.com 주소로 webhook 설정

    : https://api.telegram.org/bot\<token>/setWebhook?url=주소/\<token>



​		



