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
    ...(exerciseType === "cardio"
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
  const id = event.target.getAttribute("data-exercisesinplan-id");
  fetch("/exercises/delete_exercise", {
    method: "Delete",
    headers: {
      "Content-Type": "application/json",
    },
    // body: JSON.stringify(parseInt(id)),
    body: JSON.stringify({ id: parseInt(id) }),
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

function detailAddExerciseForm() {
  // popup form for adding details to your exercise
}

function detailAddExercise(event, inputElement) {
  const selectedValue = inputElement.value;
  const selectedOption = event.target.value;
  let wc;
  let fvalue;
  if (selectedOption == "kg" || selectedOption == "lb") {
    if (selectedOption == "lb") {
      fvalue = convertToKG(selectedValue);
    }
    wc = weight;
  } else {
    if (selectedOption == "miles") {
      fvalue = convertToKM(selectedValue);
    }
    wc = cardio;
  }
  const scheduleVal = {
    sets: 0,
    repetitions: 0,
    wc: fvalue,
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

function convertToKG(lb) {
  // for an approximate result, divide the mass value by 2.205
  return parseInt(lb) / 2.205;
}
function convertToKM(miles) {
  // for an approximate result, multiply the length value by 1.609
  return parseInt(miles) * 1.609;
}
