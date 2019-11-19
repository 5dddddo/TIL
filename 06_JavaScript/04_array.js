// web console 창에서 실습

> const numbers = [1,2,3,4,5]
> numbers[0]
1
> numbers[-1] // 양의 index만 가능
undefined 

> numbers.length
5
> numbers.reverse() // 원본 Array 자체를 reverse시킴
[5, 4, 3, 2, 1]

> numbers.reverse() 
[1,2,3,4,5]

> numbers.push('a')
6

> numbers
[1,2,3,4,5,"a"]

>numbers.pop()
"a"

> numbers.unshift('a')
6

> numbers
["a",1,2,3,4,5]

> numbers.shift()
"a"

> numbers
[1,2,3,4,5]

> numbers.push('a','b')
[1,2,3,4,5,"a","b"]

> numbers.unshift('a')
8

> numbers
["a",1,2,3,4,5,"a","b"]

> numbers.indexOf('a')
0

> numbers.indexOf('b')
7

> numbers.indexOf('c')
-1

> numbers.join()
"a,1,2,3,4,5,a,b"


> numbers.join('-')
"a-1-2-3-4-5-a-b"

> numbers.join('')
"a12345ab"
