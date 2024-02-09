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
