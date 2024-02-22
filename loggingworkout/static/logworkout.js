const unitItem = document.getElementById("exercise-left");
function addsets(event) {
  const id = event.target.parentElement;
  const lastLiInDiv = document.querySelector(
    `[id="${id.id}"] div li:last-child`
  );
  let num = lastLiInDiv.getAttribute("data-set-id");
  const weightInput = lastLiInDiv.querySelector('input[name="weight"]');
  const cardioInput = lastLiInDiv.querySelector('input[name="cardio"]');
  const repetitionsInput = lastLiInDiv.querySelector(
    'input[name="repetitions"]'
  );

  let set_type;
  if (weightInput) {
    set_type = "weight";
  } else {
    set_type = "cardio";
  }

  let setValues = {
    num: num,
    set_type: set_type,
  };
  // checking if it exist before adding to setValue to send to server
  if (weightInput) {
    setValues.weightInput = weightInput.value;
  }
  if (repetitionsInput) {
    setValues.repetitionsInput = repetitionsInput.value;
  }
  if (cardioInput) {
    setValues.cardioInput = cardioInput.value;
  }
  console.log(setValues);
  fetch(`/logging/addsets`, {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(setValues),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then((data) => {
      const placement = id.querySelector("#set-in-here");
      placement.insertAdjacentHTML("beforeend", data);
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

function logWorkout(event) {
  const parent = event.target.parentElement;
  const inputs = parent.querySelectorAll("input");

  let setValues = {};

  // get input value
  inputs.forEach((input) => {
    setValues[input.name] = input.value;
  });

  // checks value
  for (const [key, value] of Object.entries(setValues)) {
    if (value == "" || isNaN(value)) {
      return console.error();
    }
  }
  // get ids and sets if no errors
  const currentUrl = window.location.href.split("/");
  const workoutId = parent.parentElement.parentElement;
  const name = parent.parentElement.previousElementSibling;
  setValues["plan-id"] = currentUrl[currentUrl.length - 1];
  setValues["set"] = parent.getAttribute("data-set-id");
  setValues["workout-id"] = workoutId.id;
  setValues["name"] = name.textContent;

  console.log(setValues);
  if (event.target.textContent == "Finish") {
    sendLog(setValues);
    inputs.forEach((input) => (input.disabled = true));
    event.target.textContent = "Enable";
  } else if (event.target.textContent == "Edit") {
    sendEditLog(setValues);
    inputs.forEach((input) => (input.disabled = false));
    event.target.textContent = "Enable";
  } else {
    inputs.forEach((input) => (input.disabled = false));
    event.target.textContent = "Edit";
  }
}
function getvalue() {}

function deleteFinishSets() {}

function switchExercise() {}

function sendLog(setValues) {
  fetch(`/logging/logworkout`, {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(setValues),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then((data) => {
      console.log(data);
      parent.setAttribute("data-log_id", "your_log_id_value");
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
function sendEditLog(setValues) {
  fetch(`/logging/editlogworkout`, {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(setValues),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then((data) => {
      console.log(data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
