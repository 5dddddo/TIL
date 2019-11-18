// Object -> String
const jsonData = JSON.stringify({
  도현: '합기도',
  혁진: '감자',
})

console.log(jsonData)
console.log(typeof jsonData)

// String -> Object
const parseData = JSON.parse(jsonData)
console.log(parseData)
console.log(typeof parseData)