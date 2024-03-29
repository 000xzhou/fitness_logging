const schedule = document.getElementById("schedule");
const scheduleInfo = document.getElementById("schedule_info");
const deleteBtn = document.querySelectorAll(".delete-btn");
const addForm = document.getElementById("add-schedule-btn");
const editBtn = document.querySelectorAll(".edit-btn");
const editForm = document.getElementById("edit-schedule-form");
const popup = document.getElementById("popup-schedule");
const overlay = document.getElementById("overlay");

deleteBtn.forEach((btn) => btn.addEventListener("click", deleteSchedule));
addForm.addEventListener("click", addScheduleForm);
editBtn.forEach((btn) => btn.addEventListener("click", editScheduleForm));
if (editForm) {
  editForm.addEventListener("submit", editSchedule);
}

function deleteSchedule(e) {
  let parentElement = e.target.closest(".schedule-detalis");

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

  let formElements = document.getElementById("add-schedule-form").elements;
  let formData = {};
  for (let i = 0; i < formElements.length; i++) {
    let element = formElements[i];
    if (element.type === "checkbox") {
      formData[element.name] = element.checked; // true if checked, false otherwise
    } else if (element.type === "select-one" || element.type === "date") {
      formData[element.name] = element.value; // Get value for select and date inputs
    } else {
      if (element.name !== "") {
        formData[element.name] = element.value;
      }
    }
  }
  const scheduleVal = {
    formData,
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
      // scheduleInfo.innerHTML += data;
      scheduleInfo.insertAdjacentHTML("afterbegin", data);

      addEventtoBtns();
      popup.innerText = "";
      popup.style.display = "none";
      overlay.style.display = "none";
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function addScheduleForm(e) {
  // let parentElement = e.target.parentElement;

  fetch("/schedule/add_schedule")
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then((data) => {
      popup.innerHTML = data;
      popup.style.display = "block";
      overlay.style.display = "block";
      document
        .getElementById("add-schedule-form")
        .addEventListener("submit", addSchedule);
      // get date
      const datePicker = document.getElementById("datepicker");
      const today = new Date();
      const year = today.getFullYear();
      const month = String(today.getMonth() + 1).padStart(2, "0");
      const day = String(today.getDate()).padStart(2, "0");
      datePicker.value = `${year}-${month}-${day}`;
      // end date
    })
    .catch((error) => {
      console.error("There was a problem with the fetch operation:", error);
    });
}

function editScheduleForm(e) {
  // pop up for editting pop up or turn the post into an edit form
  let parentElement = e.target.closest(".schedule-detalis");

  fetch("/schedule/edit_schedule/" + parentElement.id)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then((data) => {
      popup.innerHTML = data;
      popup.style.display = "block";
      overlay.style.display = "block";
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
  let formElements = document.getElementById("edit-schedule-form").elements;
  let formData = {};
  for (let i = 0; i < formElements.length; i++) {
    let element = formElements[i];
    if (element.type === "checkbox") {
      formData[element.name] = element.checked; // true if checked, false otherwise
    } else if (element.type === "select-one" || element.type === "date") {
      formData[element.name] = element.value; // Get value for select and date inputs
    } else {
      if (element.name !== "") {
        formData[element.name] = element.value;
      }
    }
  }
  const scheduleVal = {
    formData,
  };
  const dataId = e.target.getAttribute("data-id");
  fetch("/schedule/edit_schedule/" + dataId, {
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
      document.getElementById(e.target.getAttribute("data-id")).innerHTML =
        data;
      addEventtoBtns();
      popup.innerText = "";
      popup.style.display = "none";
      overlay.style.display = "none";
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

overlay.addEventListener("click", function () {
  popup.style.display = "none";
  overlay.style.display = "none";
});
