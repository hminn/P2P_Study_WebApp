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
	var study = false;
	if (date.getHours() < 9) {
		var endDate = new Date(2020, month, clockDate, 09, 00, 00); // 종료날짜
		study = false;
	} else if (
		date.getHours() < 10 ||
		(date.getHours() < 11) & (date.getMinutes() < 45)
	) {
		var endDate = new Date(2020, month, clockDate, 10, 45, 00);
		study = true; // 종료날짜
	} else if (date.getHours() < 11) {
		var endDate = new Date(2020, month, clockDate, 11, 00, 00); // 종료날짜
		study = false;
	} else if (date.getHours() < 13) {
		var endDate = new Date(2020, month, clockDate, 13, 00, 00); // 종료날짜
		study = true;
	} else if (
		date.getHours() < 14 ||
		(date.getHours() < 15) & (date.getMinutes() < 30)
	) {
		var endDate = new Date(2020, month, clockDate, 14, 30, 00); // 종료날짜
		study = false;
	} else if (
		date.getHours() < 15 ||
		(date.getHours() < 16) & (date.getMinutes() < 45)
	) {
		var endDate = new Date(2020, month, clockDate, 15, 45, 00); // 종료날짜
		study = true;
	} else if (date.getHours() < 16) {
		var endDate = new Date(2020, month, clockDate, 16, 00, 00); // 종료날짜
		study = false;
	} else if (date.getHours() < 18) {
		var endDate = new Date(2020, month, clockDate, 18, 00, 00); // 종료날짜
		study = true;
	} else {
		var endDate = new Date(); // 종료날짜
		study = false;
	}
	var remaining_time = endDate - date;
	var time_out = date - endDate;
	var timerTarget = document.getElementById("timetable");
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
	if (study == true) {
		timerTarget.innerText = "지금은 학습시간 입니다 - " + `${timer}`;
	} else {
		timerTarget.innerText = "지금은 휴식시간 입니다 - " + `${timer}`;
	}
	setTimeout(study_timer, 1000);
}
