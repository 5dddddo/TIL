// 숫자가 담긴 배열의 요소에 각각 2를 곱하여 새로운 배열 만들기

// ES5
var numbers = [1, 2, 3]
var doubleNumbers = []

for (var i = 0; i < numbers.length; i++) {
  doubleNumbers.push(numbers[i] * 2)
}
console.log(doubleNumbers)
console.log(numbers) // 원본 유지

// ES6+
const NUMBERS = [1, 2, 3]
// const DOUBLENUMBERS = []
NUMBERS.map(function (number) {
  return number * 2
})

const DOUBLENUMBERS = NUMBERS.map(number => number * 2)
console.log(DOUBLENUMBERS)

// map 헬퍼를 사용해서 images 배열 안의 객체들의 height들만 저장 되어 있는 배열을 만들어보자
const images = [{
  height: '34px',
  width: '59px'
}, {
  height: '11px',
  width: '35px'
}, {
  height: '87px',
  width: '19px'
}]

const heights = images.map(image => image.height)
console.log(heights)

// map 핼퍼를 사용해서 "distance/time => 속도"를 저장하는 새로운 배열 speeds를 만들어보자

const trips = [{
  distance: 34,
  time: 15
}, {
  distance: 64,
  time: 18
}, {
  distance: 96,
  time: 34
}]

const speeds = trips.map(trip => trip.distance / trip.time)
console.log(speeds)