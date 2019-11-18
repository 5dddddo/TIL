// // ES5 버전
// var books = ['자바스크립트 입문', '장고 웹 프로그래밍']
// var comics = {
//   'DC': ['Aquaman', 'Joker'],
//   'Marvel': ['Avengers', 'Spider man']
// }
// var magazines = null

// var bookShop = {
//   books: books,
//   comics: comics,
//   magazines: magazines
// }

// console.log(bookShop)
// console.log(typeof bookShop)
// console.log(bookShop.books[0])

// ES6 이후
// 객체의 key와 value가 똑같으면 , 마치 배열처럼 한 번만 작성 가능
let books = ['자바스크립트 입문', '장고 웹 프로그래밍']
let comics = {
  'DC': ['Aquaman', 'Joker'],
  'Marvel': ['Avengers', 'Spider man']
}
let magazines = null

const bookShop = {
  books,
  comics,
  magazines
}

console.log(bookShop)
console.log(typeof bookShop)
console.log(bookShop.books[0])