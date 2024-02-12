import { convertToKG, convertToKM } from "./helpers";

function addToSchedule(event) {
  const planElement = document.getElementById("schedule-id");
  const planId = planElement.getAttribute("data-plan-id");
  const scheduleVal = {
    plan_id: planId,
    exercise_id: event.target.getAttribute("data-exercise-id"),
    exercise_name: event.target.getAttribute("data-exercise-name"),
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
  if (selectedOption == "kg" || selectedOption == "lb") {
    if (selectedOption == "lb") {
      convertToKG(selectedValue);
    }
    wc = weight;
  } else {
    if (selectedOption == "miles") {
      convertToKM(selectedValue);
    }
    wc = cardio;
  }
  const scheduleVal = {
    sets: 0,
    repetitions: 0,
    wc: selectedValue + selectedOption,
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
