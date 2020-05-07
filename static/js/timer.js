function toHourMinSec(t) {
	// 정수로부터 남은 시, 분, 초 단위 계산
	var hours = Math.floor((time % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
	var mins = Math.floor((time % (1000 * 60 * 60)) / (1000 * 60));
	var secs = Math.floor((time % (1000 * 60)) / 1000);
	// hh:mm:ss 형태를 유지하기 위해 한자리 수일 때 0 추가
	if (hours < 10) hours = "0" + hours;
	if (mins < 10) mins = "0" + mins;
	if (secs < 10) secs = "0" + secs;
	return hours + ":" + mins + ":" + secs;
}
function study_timer() {
	var date = new Date();
	var month = date.getMonth();
	var clockDate = date.getDate();
	var endDate = new Date(2020, month, clockDate, 19, 00, 00); // 종료날짜
	var remaining_time = endDate - date;
	var time_out = date - endDate;
	var timerTarget = document.getElementById("timetable");
	// 조건문 추후 활용 예정
	// if (hours < 12) {
	//     hours = "AM";
	// }
	// else {
	//     hours = "PM";
	// }
	// 정수로부터 남은 시, 분, 초 단위 계산
	if (remaining_time >= 0) {
		var hours = Math.floor(
			(remaining_time % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
		);
		var mins = Math.floor((remaining_time % (1000 * 60 * 60)) / (1000 * 60));
		var secs = Math.floor((remaining_time % (1000 * 60)) / 1000);
	} else {
		var hours = Math.floor(
			(time_out % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
		);
		var mins = Math.floor((time_out % (1000 * 60 * 60)) / (1000 * 60));
		var secs = Math.floor((time_out % (1000 * 60)) / 1000);
	}
	// hh:mm:ss 형태를 유지하기 위해 한자리 수일 때 0 추가
	if (hours < 10) hours = "0" + hours;
	if (mins < 10) mins = "0" + mins;
	if (secs < 10) secs = "0" + secs;
	var timer = hours + ":" + mins + ":" + secs;
	if (remaining_time >= 0) {
		timerTarget.innerText = "남은 시간 - " + `${timer}`;
	} else {
		timerTarget.innerText = "초과 시간 - " + `${timer}`;
	}
	setTimeout(study_timer, 1000);
}
