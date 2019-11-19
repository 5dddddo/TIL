// for loop 활용
var students = [{
    name: '서혁진',
    type: 'male'
  },
  {
    name: '이도현',
    type: 'female'
  }, {
    name: '황민승',
    type: 'male'
  }, {
    name: '공선아',
    type: 'female'
  }
]


var strongStudents = []
for (var i = 0; i < students.length; i++) {
  if (students[i].type === 'female') {
    strongStudents.push(students[i])
  }
}
console.log(students) // 원본 유지
console.log(strongStudents) // 새로운 배열
console.log(students[1].name) // 객체 내 속성 접근


const STUDENTS = [{
    name: '서혁진',
    type: 'male'
  },
  {
    name: '이도현',
    type: 'female'
  }, {
    name: '황민승',
    type: 'male'
  }, {
    name: '공선아',
    type: 'female'
  }
]

// STUDENTS 배열의 객체들 중 type이 female인 요소만 뽑기
// STUDENTS 배열 자체를 바꾸고 싶은 것이 아니라,
// 원하는 조건에 맞는 새로운 배열을 만들어보자
const STRONGSTUDENTS1 = STUDENTS.filter(function (student) {
  return student.type === 'female'
})

const STRONGSTUDENTS2 = STUDENTS.filter(student => student.type === 'female')
console.log(STUDENTS) // 원본 유지
console.log(STRONGSTUDENTS2) // 새로운 배열

// filter를 사용해서 numbers 배열 중 50보다 큰 값만 필터링해서 새로운 배열에 저장하기
const numbers = [15, 30, 8, 4, 68, 1, 11, 88, 76, 54, 5]
const newNumbers = numbers.filter(number => number > 50)
console.log(newNumbers)