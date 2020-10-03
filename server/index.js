const PORT = process.env.PORT || 5000

const express = require('express')
const bodyParser = require('body-parser')
const path = require('path')

const Cluster = require('./cluster')

const app = express()
const cluster = new Cluster()

app
    .use(bodyParser.json())
    .use(bodyParser.urlencoded())
    .use(express.static('client'))


app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '/client/index.html'))
})

app.get('/api/shouldWait', (req, res) => {
    res.json({ wait: cluster.shouldWait() })
})

app.get('/api/shouldContinue', (req, res) => {
    res.json({ continue: cluster.shouldContinue() })
})

app.get('/api/config', (req, res) => {
    res.json({ blockSize: cluster.blockSize, startTime: cluster.startTime, endTime: cluster.endTime })
})

app.get('/api/next', (req, res) => {
    res.json({ next: cluster.next() })
})

app.get('/api/status', (req, res) => {
    res.json({ testCount: cluster.testCount, failedTests: cluster.failedTests })
})

app.post('/api/status', (req, res) => {
    if (Object.keys(req.body).length >= 2) {
        console.log(req.body)
        cluster.updateTestCount(req.body)
        res.sendStatus(200)
    } else {
        res.sendStatus(400)
    }
})

app.listen(PORT, () => { console.log('Listening on ', PORT) })