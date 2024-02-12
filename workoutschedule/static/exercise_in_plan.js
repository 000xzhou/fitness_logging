// import { convertToKG, convertToKM } from "./helpers.js";

function addToSchedule(event) {
  const planElement = document.getElementById("schedule-id");
  const planId = planElement.getAttribute("data-plan-id");
  const exerciseType = event.target.getAttribute("data-exercise-category");
  const scheduleVal = {
    plan_id: planId,
    exercise_id: event.target.getAttribute("data-exercise-id"),
    exercise_name: event.target.getAttribute("data-exercise-name"),
    // adding exercise base on type
    ...(exerciseType === "Cardio"
      ? { sets: 1, cardio: 10 }
      : { sets: 3, rep: 10, weight: 10 }),
  };
  fetch("/exercises/add_exercise", {
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
      exercisesinplan.innerHTML += data;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function deleteFromSchedule(event) {
  const id = event.target.parentElement;
  fetch("/exercises/delete_exercise", {
    method: "Delete",
    headers: {
      "Content-Type": "application/json",
    },
    // body: JSON.stringify(parseInt(id)),
    body: JSON.stringify({ id: parseInt(id.id) }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      if ((data.message = "Schedule deleted successfully")) {
        event.target.parentElement.remove();
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function detailEditExerciseForm(event) {
  // turn the things under exerice name into form
  const id = event.target.parentElement;

  fetch(`/exercises/edit_exercise/${id.id}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then((data) => {
      id.innerHTML = data;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function detailEditExercise(event) {
  event.preventDefault();
  const id = event.target.parentElement.getAttribute("data-id");
  let formElements = event.target.parentElement.elements;
  let formData = {};
  for (let i = 0; i < formElements.length; i++) {
    let element = formElements[i];
    if (element.name !== "") {
      formData[element.name] = element.value;
    }
  }
  const scheduleVal = {
    formData,
  };
  fetch(`/exercises/edit_exercise/${id}`, {
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
      event.target.parentElement.parentElement.innerHTML = data;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function convertToKG(lb) {
  // for an approximate result, divide the mass value by 2.205
  return parseInt(lb) / 2.205;
}
function convertToKM(miles) {
  // for an approximate result, multiply the length value by 1.609
  return parseInt(miles) * 1.609;
}
