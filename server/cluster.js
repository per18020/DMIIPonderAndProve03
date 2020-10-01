class Cluster {
    constructor() {
        this.testCount = 0
        this.failedTests = []
        this.increment = 0
        this.blockSize = 100000000
        this.startTime = new Date("2020-10-02T18:00:00.000Z")
        this.endTime = new Date("2020-10-03T18:00:00.000Z")
    }

    updateTestCount({testCount, didSucceed}) {
        if (didSucceed) {
            this.testCount = testCount > this.testCount ? testCount : this.testCount
        } else {
            this.failedTests.push(testCount)
        }
    }

    shouldWait() {

        // TODO REMOVE THIS
        return false

        const currentTime = new Date()
        return currentTime < this.startTime
    }

    shouldContinue() {
        const currentTime = new Date()
        return !this.shouldWait() && currentTime < this.endTime
    }

    next() {
        const savedIncrement = this.increment
        this.increment++
        return savedIncrement
    }
}

module.exports = Cluster