const calendarDay = document.querySelectorAll(".calendar-day");
const eventsHTML = document.getElementById("events");

let lastClickedDay = null;
calendarDay.forEach((day) =>
  day.addEventListener("click", () => {
    if (lastClickedDay) {
      // lastClickedDay.style.color = "";
      lastClickedDay.classList.remove("clicked-day");
      eventsHTML.innerHTML = "";
    }
    day.classList.add("clicked-day");
    lastClickedDay = day;

    let calenderevents = day.querySelectorAll(".calendar-events");
    if (calenderevents.length !== 0) {
      let events = "";
      calenderevents.forEach((event) => {
        events += `<li>${event.textContent}</li>`;
      });
      eventsHTML.innerHTML = `<ul>${events}</ul>`;
    }
  })
);
