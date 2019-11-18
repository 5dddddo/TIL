const me = {
  name: 'ㅇㅇ', // key가 한 단어일 때
  'phone number': '01012345678', // key가 여러 단어일 때
  appleProducts: {
    iphone: 'xs',
    watch: 'series5',
    macbook: 'pro2019'
  }
}

console.log(me.name)

// key가 여러 단어일 때, []로 접근
console.log(me['phone number'])

console.log(me.appleProducts)

console.log(me.appleProducts.iphone)