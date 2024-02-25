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

function setBtn(event) {
  const btnText = event.target;
  const parent = btnText.parentElement;
  const inputs = parent.querySelectorAll("input");
  if (btnText.textContent == "Done") {
    inputs.forEach((input) => (input.disabled = true));
    btnText.textContent = "Enable";
  } else if (btnText.textContent == "Edit") {
    inputs.forEach((input) => (input.disabled = true));
    btnText.textContent = "Enable";
  } else {
    inputs.forEach((input) => (input.disabled = false));
    btnText.textContent = "Edit";
  }
}

// ======================= TIMER ==========================================
const timerDiv = document.getElementById("timer");
timerDiv.addEventListener("click", toggleTimer);
let timer;
let startTime;
let running = false;
let elapsedTime = 0;

function toggleTimer() {
  if (!running) {
    startTimer();
    console.log("start");
  } else {
    pauseTimer();
    console.log("stop");
  }
}

function startTimer() {
  running = true;
  startTime = Date.now() - elapsedTime;
  timer = setInterval(updateTimer, 1000);
}

function pauseTimer() {
  running = false;
  clearInterval(timer);
  updateStopTimer();
  elapsedTime = Date.now() - startTime;
}

function updateTimer() {
  elapsedTime = Date.now() - startTime;
  timerDiv.innerHTML = `${formatTime(elapsedTime)} <span>stop icon</span>`;
}
function updateStopTimer() {
  elapsedTime = Date.now() - startTime;
  timerDiv.innerHTML = `${formatTime(elapsedTime)} <span>start icon</span>`;
}

function formatTime(milliseconds) {
  const totalSeconds = Math.floor(milliseconds / 1000);
  const minutes = Math.floor(totalSeconds / 60);
  const seconds = totalSeconds % 60;
  return `${minutes}:${seconds < 10 ? "0" : ""}${seconds}`;
}
function formatTimeData(milliseconds) {
  const totalSeconds = Math.floor(milliseconds / 1000);
  return totalSeconds;
}

// ==================== get value from form =================================================
const logBtn = document.getElementById("log-info");
logBtn.addEventListener("click", getvalue);

function getvalue() {
  // confirming
  if (confirm("Are you sure you want to finish this workout?")) {
    // get value
    const form = document.getElementById("logging-info-form");
    // stop timer if it's still running
    if (running) {
      pauseTimer();
    }
    let setValues = {};
    let exerciseId = {};
    let notes;
    let duration;
    let items = form.children;
    for (let i = 0; i < items.length; i++) {
      let name = items[i].querySelector("h3");
      let lis = items[i].querySelectorAll("li");
      lis.forEach((li) => {
        let btnName = li.querySelector("button");
        if (btnName.textContent == "Enable") {
          setValues[name.textContent] = {};
          exerciseId[name.textContent] = items[i].id;
        }
      });
      lis.forEach((li) => {
        let btnName = li.querySelector("button");
        if (btnName.textContent == "Enable") {
          const set = li.getAttribute("data-set-id");
          setValues[name.textContent][set] = {};

          const inputs = li.querySelectorAll("input");
          inputs.forEach((input) => {
            setValues[name.textContent][set][input.name] = input.value;
          });
        }
      });
    }
    if (Object.keys(setValues).length === 0) {
      console.log("empty");
    } else {
      duration = formatTimeData(elapsedTime);
      let note = window.prompt("Any additional notes: ", "");
      if (note == null || note == "") {
        console.log("No additional notes added.");
      } else {
        notes = note;
      }
      // console.log(setValues);
      // console.log(exerciseId);
      // console.log(formatTimeData(elapsedTime));
      sendLog(setValues, exerciseId, duration, notes);
    }
  } else {
    console.log("nothing happend");
  }
}

function switchExercise() {}

function sendLog(setValues, exerciseId, duration, notes) {
  fetch(`/logging/logworkout`, {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      setValues: setValues,
      exerciseId: exerciseId,
      duration: duration,
      notes: notes,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      window.location.href = "/dashboard";
      // return response.text();
    })
    .then((data) => {
      console.log(data);
      // parent.setAttribute("data-log_id", "your_log_id_value");
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

function startExercise() {}
