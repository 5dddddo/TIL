# 191119_JavaScript Syntax basics 2

## 8. Array Helper Method

> [08_forEach.js](https://github.com/5dddddo/TIL/blob/master/06_JavaScript/08_forEach.js) 참고

- Helper란 자주 사용하는 로직을 재활용 할 수 있게 만든 일종의 library
- ES6부터 본격적으로 사용됨
- 상세한 사용법 : **MDN** 문서 참고

### 8.1 `forEach`

- `arr.forEach(callback(element, index, array))`

  - 주어진 callback 함수를 **배열에 있는 각 요소에 대해 한 번씩 실행**

  ```javascript
  // ES5 for loop
  var iot1 = ['도현', '혁진', '은애']
  for (var i = 0; i < iot1.length; i++) {
    console.log(iot[i])
  }
  
  // ES6+
  const IOT1 = ['수연', '선아', '주현']
  IOT1.forEach(function (student) {
    console.log(student)
  })
  
  // 한 줄로 리팩토링 가능
  IOT1.forEach(student => console.log(student))
  
  const res = IOT1.forEach(student => console.log(student))
  > console.log(res)
  undefined
  ```

- [실습] for를 forEach로 바꾸기

  ```javascript
  function handleStudents() {
    const students = [{
      id: 1,
      name: '오은애',
      status: '응애?'
    }, {
      id: 15,
      name: '서혁진',
      status: '감자?'
    }, {
      id: 28,
      name: '김영선',
      status: '쉽다쉬훠'
    }]
  
    // for (let i = 0; i < students.length; i++) {
    //   console.log(students[i])
    //   console.log(students[i].name)
    //   console.log(students[i].status)
    // }
    students.forEach(student => console.log(student, student.name, student.status))
  }
  ```

- [실습] images 배열 안에 있는 정보를 곱해 넓이를 구하여 areas 배열에 저장

  ```javascript
  const images = [{
      height: 30,
      width: 55
    },
    {
      height: 50,
      width: 178
    },
    {
      height: 81,
      width: 35
    }
  ]
  const areas = []
  
  images.forEach(image =>
    areas.push(image.height * image.width)
  )
  
  > console.log(areas)
  [ 1650, 8900, 2835 ]
  ```

  <br>

## 8.2 `map`

> 09_map.js 참고

- arr.map(callback(element))

- 배열 내의 모든 요소에 대하여 주어진 콜백 함수를 호출한 결과를 모아 새로운 배열 return

- `map`,`filter` 둘 다 사본을 return하고 **원본은 바뀌지 않음**

  - 만약, **return을 안 적으면 undefined가 발생**함

- [실습] 숫자가 담긴 배열의 요소에 각각 2를 곱하여 새로운 배열 만들기

  ```javascript
  // ES5
  var numbers = [1, 2, 3]
  var doubleNumbers = []
  
  for (var i = 0; i < numbers.length; i++) {
    doubleNumbers.push(numbers[i] * 2)
  }
  
  > console.log(doubleNumbers)
  [ 2, 4, 6 ]
  
  > console.log(numbers) // 원본 유지
  [ 1, 2, 3 ]
  
  // ES6+
  const NUMBERS = [1, 2, 3]
  // const DOUBLENUMBERS = []
  
  // 1. 일반적인 함수
  NUMBERS.map(function (number) {
    return number * 2
  })
  
  // 2. 화살표 함수
  const DOUBLENUMBERS = NUMBERS.map(number => number * 2)
  > console.log(DOUBLENUMBERS)
  [ 2, 4, 6 ]
  ```

<br>

- [실습] map 헬퍼를 사용해서 images 배열에서 height들만 추출한 배열을 만들어보자

  ``` javascript
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
  > console.log(heights)
  [ '34px', '11px', '87px' ]
  ```

- [실습] "distance/time => 속도"를 저장하는 새로운 배열 speeds를 만들어보자

  ```javascript
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
  > console.log(speeds)
  [ 2.2666666666666666, 3.5555555555555554, 2.823529411764706 ]
  ```

<br>

## 8.3 `filter`

- `arr.filter(callback(element))`
- 주어진  callback 함수의 **테스트를 통과하는 모든 요소**를 모아서 새로운 배열로 반환
  - 즉, callback 함수에 조건을 적어서 **원하는 요소들만 filtering**
  - 