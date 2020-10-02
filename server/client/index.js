function run() {
    getConfig()
    update()
    setInterval(update, 5000)
}

function getConfig() {
    fetch('/api/config').then(res => res.json()).then(res => {
        document.getElementById('startTimeDisplay').value = new Date(res.startTime)
        document.getElementById('endTimeDisplay').value = new Date(res.endTime)
        document.getElementById('blockSizeDisplay').value = res.blockSize
    })
}

function update() {
    fetch('/api/status').then(res => res.json()).then((res) => {
        document.getElementById('testCountDisplay').value = res.testCount
        document.getElementById('testFailedDisplay').value = res.failedTests.length
    })
}

window.onload = run