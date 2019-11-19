// let(변수)
let x = 1
// let x = 3 // Error : Identifier 'x' has already been declared

// x = 3 // 재할당
// console.log(x)

if (x === 1) {
  let x = 2
  console.log(x)
}
console.log(x)

// const(상수)
// 초기화를 생략하면 Error
// const MY_FAV
// MY_FAV를 상수로 정의하고 그 값을 7로 설정
const MY_FAV = 7
console.log(MY_FAV)

// 상수 재할당 에러 -> Assignment
// MY_FAV = 10
// 상수 재선언 에러
// const MY_FAV = 20
// let MY_FAV = 11
if (MY_FAV === 7) {
  const MY_FAV = 11
  console.log(MY_FAV)
}
console.log(MY_FAV)