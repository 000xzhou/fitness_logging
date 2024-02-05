const popupContainer = document.getElementById("popupContainer");
const editBtn = document.querySelectorAll(".edit-btn");
const deleteBtn = document.querySelectorAll(".delete-btn");
const addForm = document.getElementById("add-schedule");
const schedule = document.getElementById("schedule");

deleteBtn.forEach((btn) => btn.addEventListener("click", deleteSchedule));
addForm.addEventListener("submit", addSchedule);

function deleteSchedule(e) {
  let parentElement = e.target.parentElement;
  const scheduleId = {
    id: parentElement.id,
  };
  fetch("/schedule/delete_schedule", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(scheduleId),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      if (data.message == "Schedule deleted successfully") {
        parentElement.remove();
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function addSchedule(e) {
  e.preventDefault();
  let nameVal = document.getElementById("add_schedule-name");
  let descriptionVal = document.getElementById("add_schedule-description");
  const scheduleVal = {
    name: nameVal.value,
    description: descriptionVal.value,
  };
  fetch("/schedule/add_schedule", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(scheduleVal),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then((data) => {
      schedule.innerHTML += data;
      addEventtoBtns();
      nameVal.value = "";
      descriptionVal.value = "";
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function addEventtoBtns() {
  const deleteBtns = document.querySelectorAll(".delete-btn");
  deleteBtns.forEach((btn) => btn.addEventListener("click", deleteSchedule));
}
