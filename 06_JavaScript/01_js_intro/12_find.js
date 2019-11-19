var students = [{
  name: '서혁진',
  age: 26
}, {
  name: '오은애',
  age: 25
}, {
  name: '이도현',
  age: 25
}, {
  name: '공선아',
  age: 25
}, {
  name: '최주현',
  age: 27
}]

var student;

for (var i = 0; i < students.length; i++) {
  if (students[i].age === 25) {
    student = students[i]
    break // 원하는 조건에 도달하면 loop 탈출
  }
}

console.log(student)

const STUDENTS = [{
  name: '서혁진',
  age: 26
}, {
  name: '오은애',
  age: 25
}, {
  name: '이도현',
  age: 25
}, {
  name: '공선아',
  age: 25
}, {
  name: '최주현',
  age: 27
}]

const s = STUDENTS.find(function (student) {
  return student.age === 27
})

console.log(s)