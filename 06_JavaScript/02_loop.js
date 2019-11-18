// while loop
// while 키워드 뒤에 나오는 조건이 true일 때 반복

let i = 0
while (i < 6) {
  console.log(i++)
}

// for loop
// javascript의 가장 기본적인 반복문
// for문에서 사용할 변수 하나를 정의하고,
//  그 변수가 특정 조건에 false 값이 될 때까지 연산 & 반복

for (let j = 0; j < 6; j++) {
  console.log(j++)
}

// python의 for in 문법과 비슷하게 사용 가능
const numbers = [1, 2, 3, 4, 5]
for(let number of numbers){
  console.log(number)
}

for(let number of [1, 2, 3, 4, 5]){
  console.log(number)
}
