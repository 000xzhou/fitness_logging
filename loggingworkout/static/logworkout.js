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

function logWorkout(event) {
  console.log("finish");
}

function deleteFinishSets() {}

function switchExercise() {}
