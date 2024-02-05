const schedule = document.getElementById("schedule");
const deleteBtn = document.querySelectorAll(".delete-btn");
const addForm = document.getElementById("add-schedule");
const editBtn = document.querySelectorAll(".edit-btn");
const editForm = document.getElementById("edit-schedule-form");

deleteBtn.forEach((btn) => btn.addEventListener("click", deleteSchedule));
addForm.addEventListener("submit", addSchedule);
editBtn.forEach((btn) => btn.addEventListener("click", editScheduleForm));
if (editForm) {
  editForm.addEventListener("submit", editSchedule);
}

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

function editScheduleForm(e) {
  // pop up for editting pop up or turn the post into an edit form
  let parentElement = e.target.parentElement;
  fetch("/schedule/edit_schedule/" + parentElement.id)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then((data) => {
      parentElement.innerHTML = data;
      document
        .getElementById("edit-schedule-form")
        .addEventListener("submit", editSchedule);
    })
    .catch((error) => {
      console.error("There was a problem with the fetch operation:", error);
    });
}

function editSchedule(e) {
  e.preventDefault();
  let parentElement = e.target.parentElement;
  let nameVal = document.getElementById("add-name");
  let descriptionVal = document.getElementById("add-description");
  console.log(nameVal);
  console.log(nameVal.value);
  const scheduleVal = {
    name: nameVal.value,
    description: descriptionVal.value,
  };
  fetch("/schedule/edit_schedule/" + parentElement.id, {
    method: "PATCH",
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
      console.log(data);
      parentElement.innerHTML = data;
      addEventtoBtns();
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function addEventtoBtns() {
  const deleteBtns = document.querySelectorAll(".delete-btn");
  deleteBtns.forEach((btn) => btn.addEventListener("click", deleteSchedule));
  const editBtns = document.querySelectorAll(".edit-btn");
  editBtns.forEach((btn) => btn.addEventListener("click", editScheduleForm));
}
