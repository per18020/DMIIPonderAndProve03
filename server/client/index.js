let config = null

function start() {
    getConfig()
    update()
    setInterval(update, 5000)
}

function getConfig() {
    fetch('/api/config').then(res => res.json()).then(res => {
        config = res
        document.getElementById('startTimeDisplay').value = new Date(res.startTime)
        document.getElementById('endTimeDisplay').value = new Date(res.endTime)
        document.getElementById('blockSizeDisplay').value = res.blockSize
    })
}

function update() {
    fetch('/api/status').then(res => res.json()).then((res) => {
        setStatusDisplay(['waitingDisplay', 'runningDisplay', 'finishedDisplay'], false)
        if (Object.keys(config).length >= 3) {
            const currentTime = new Date()
            if (currentTime < new Date(config.startTime)) {
                setStatusDisplay(['waitingDisplay'], true)
            }
            if (currentTime > new Date(config.startTime) && currentTime < new Date(config.endTime)) {
                setStatusDisplay(['runningDisplay'], true)
            }
            if (currentTime > new Date(config.endTime)) {
                setStatusDisplay(['finishedDisplay'], true)
            }
        }
        document.getElementById('testCountDisplay').value = res.testCount
        document.getElementById('testFailedDisplay').value = res.failedTests.length
    })
}

function setStatusDisplay(ids, value) {
    ids.forEach(id => {
        const element = document.getElementById(id)
        element.disabled = !value
        if (value) {
            element.classList.add('is-current')
        } else {
            element.classList.remove('is-current')
        }
    })
}

window.onload = start