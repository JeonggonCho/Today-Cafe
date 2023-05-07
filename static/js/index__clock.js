const clock = document.querySelector(".index__clock")

const zeroTime = function (num) {
    const numTime = parseInt(num)
    let answer = (numTime < 10) ? String(num).padStart(2, "0") : num
    return answer
}

//12시간 기준 hour 변환
const twelveHour = function (num) {
    let numHour = parseInt(num)
    let hour = ''
    let amPm = 'AM'
    amPm = numHour < 13 ? "AM" : "PM"
    numHour = numHour < 13 ? numHour : (numHour - 12)
    hour = numHour < 10 ? String(numHour).padStart(2, "0") : String(numHour)
    if (amPm === "AM" && hour === "00") {hour = "12"}
    // num이 언제나 string이라는 보장이 없기에 반드시 String에 씌워서 padStart 메서드를 적용해야한다.
    return (amPm + ' ' + hour)
}

const getClock = function () {
    const date = new Date()
    const hour = twelveHour(date.getHours())
    const minute = zeroTime(date.getMinutes())
    const second = zeroTime(date.getSeconds())
    clock.innerText = `${hour} : ${minute} : ${second}`
}

getClock()
let twentyFourInterval = setInterval(getClock, 1000)