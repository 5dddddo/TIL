const tests = [90, 80, 77, 13, 58]
const sum1 = test.reduce(function (total, score) {
  return total += score
})

const sum2 = test.reduce((total, score) => total += score)
console.log(sum2)