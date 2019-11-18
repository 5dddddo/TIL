// 선언식
// 코드가 실행되기 전에 load 됨

console.log(add(3, 5))

function add(num1, num2) {
  return num1 + num2
}
console.log(add(1, 2))

// 표현식 : 함수를 변수에 담기
// 코드가 실행된 후 load 됨
// console.log(sub(3,1)) -> Error

const sub = function (num1, num2) {
  return num1 - num2
}
console.log(sub(4, 2))

// 타입 확인하면 둘 다 function type
// 동작 방법만 다름
console.log(typeof add)
console.log(typeof sub)

// 화살표 함수 (Arrow function)
const iot = function (name) {
  return `hello, ${name}!!`
}

// 1. function 키워드 삭제
const iot1 = (name) => {
  return `hello, ${name}!!`
}

// 2. () 생략 (함수 매개변수가 하나일 경우)
const iot2 = name => {
  return `hello, ${name}!!`
}

// 3. {}, return 생략 (함수 바디에 표현식이 하나일 경우)
const iot3 = (name) => `hello, ${name}!!`

//[실습] 3단계에 걸쳐서 화살표 함수로 바꿔보자
let square = function (num) {
  return num ** 2
}

square = (num) => {
  return num ** 2
}

square = num => {
  return num ** 2
}

square = num => num ** 2

console.log(square(5))

// 4. 인자가 없다면 : () 혹은 _ 로 표시 가능
let noArgs = () => 'No args'
noArgs = _ => 'no args!!@'
noArgs()

// 5-1. object를 return을 명시적으로 적어줌
let returnObject1 = () => { return { key: 'value' } }

console.log(returnObject1())
console.log(typeof returnObject1())

// 5-2. return을 적지 않으려면 괄호 붙이기
let returnObject2 = () => ({  key: 'value' })

console.log(returnObject2())
console.log(typeof returnObject2())

//6. 기본 인자 부여하기 (Default Args)
//인자 개수와 상관 없이 반드시 괄호를 붙인다
const sayHello = (name='혁진') => 'hi! ${name}'

// 6. 익명 / 1회용 함수 (Anonymous function)
// 