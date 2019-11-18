// // ES5 for loop
// var iot1 = ['도현', '혁진', '은애']
// for (var i = 0; i < iot1.length; i++) {
//   console.log(iot1[i])
// }

// // ES6+
// const IOT1 = ['수연', '선아', '주현']
// IOT1.forEach(function (student) {
//   console.log(student)
// })

// // 한 줄로 리팩토링 가능
// IOT1.forEach(student => console.log(student))

// const res = IOT1.forEach(student => console.log(student))
// console.log(res)

// // [실습] for를 forEach로 바꾸기
// function handleStudents() {
//   const students = [{
//     id: 1,
//     name: '오은애',
//     status: '응애?'
//   }, {
//     id: 15,
//     name: '서혁진',
//     status: '감자?'
//   }, {
//     id: 28,
//     name: '김영선',
//     status: '쉽다쉬훠'
//   }]

//   for (let i = 0; i < students.length; i++) {
//     console.log(students[i])
//     console.log(students[i].name)
//     console.log(students[i].status)
//   }

//   students.forEach(student => console.log(student, student.name, student.status))
// }

// handleStudents()

// [실습] images 배열 안에 있는 정보를 곱해 넓이를 구하여 areas 배열에 저장
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

console.log(areas)