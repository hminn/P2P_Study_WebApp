function showClock() {
	var date = new Date();
	var month = date.getMonth();
	var clockDate = date.getDate();
	var day = date.getDay();
	var week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
	var hours = date.getHours();
	var minutes = date.getMinutes();
	var seconds = date.getSeconds();
	var clockTarget = document.getElementById("clock");
	if (hours > 9) {
		clockTarget.style.color = "black";
	} else {
		clockTarget.style.color = "white";
	}
	clockTarget.innerText =
		`${month + 1}월 ${clockDate}일 ${week[day]}` +
		"\n" +
		`${hours < 10 ? `0${hours}` : hours}:${
			minutes < 10 ? `0${minutes}` : minutes
		}:${seconds < 10 ? `0${seconds}` : seconds}`;
	setTimeout(showClock, 1000);
}
