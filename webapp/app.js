const express = require('express')
const app = express()
const axios = require('axios');

const path = ''
const url = 'http://localhost:5000/api_v2'

app.get('/axios', async function(req, res) {
    const data = await axios.post(url, { 'path' : path })
    res.send(data.data)
})

app.get('/', function(req, res) {
    res.send('Hello hehe !')
})

app.listen(3000)