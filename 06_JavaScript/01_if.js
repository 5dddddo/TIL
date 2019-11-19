// web console 창에서 실습

const userName = prompt('니 이름은 뭐니?')
// 이름 입력

let message = ''
if (userName ==='도현'){
    message = '유단자'
}else if(userName === '혁진'){
    message = '감자'
}else{
    // 값을 불러오려면 ` `로 감싸기
	message = `<h1> ${userName}..누구?</h1>`
}
document.write(message)
