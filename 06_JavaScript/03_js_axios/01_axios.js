const axios = require('axios')

axios.get('https://jsonplaceholder.typicode.com/posts/1')
  .then(response => {
    console.log(response)
  })
  .catch(error => {
    console.log(error)
  })