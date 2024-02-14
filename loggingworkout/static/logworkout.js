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
  if (event.target.textContent == "Enable") {
    inputs.forEach((input) => (input.disabled = false));
    event.target.textContent = "Edit";
  } else {
    inputs.forEach((input) => (input.disabled = true));
    event.target.textContent = "Enable";

    const unit = unitItem.getAttribute("data-unit");
    // get values
    let setValues = {};
    inputs.forEach((input) => {
      if (unit == "metric") {
        setValues[input.name] = input.value;
      } else {
        if (input.name == "weight") {
          setValues[input.name] = convertToKG(input.value);
        } else if (input.name == repetitions) {
          setValues[input.name] = input.value;
        } else {
          setValues[input.name] = convertToKM(input.value);
        }
      }
    });
    console.log(setValues);
    // log the workout
    // fetch(`/logging/logworkout`, {
    //   method: "post",
    //   headers: {
    //     "Content-Type": "application/json",
    //   },
    //   body: JSON.stringify(setValues),
    // })
    //   .then((response) => {
    //     if (!response.ok) {
    //       throw new Error("Network response was not ok");
    //     }
    //     return response.text();
    //   })
    //   .then((data) => {
    //     const placement = id.querySelector("#set-in-here");
    //     placement.insertAdjacentHTML("beforeend", data);
    //   })
    //   .catch((error) => {
    //     console.error("Error:", error);
    //   });
  }
}

function deleteFinishSets() {}

function switchExercise() {}
