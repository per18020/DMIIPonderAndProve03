const PORT = process.env.PORT || 5000

const express = require('express')
const bodyParser = require('body-parser')

const Cluster = require('./cluster')

const app = express()
const cluster = new Cluster()

app
    .use(bodyParser.json())
    .use(bodyParser.urlencoded())


app.get('/api/shouldWait', (req, res) => {
    res.json({ wait: cluster.shouldWait() })
})

app.get('/api/shouldContinue', (req, res) => {
    res.json({ continue: cluster.shouldContinue() })
})

app.get('/api/config', (req, res) => {
    res.json({ blockSize: cluster.blockSize })
})

app.get('/api/next', (req, res) => {
    res.json({ next: cluster.next() })
})

app.listen(PORT, () => { console.log('Listening on ', PORT) })