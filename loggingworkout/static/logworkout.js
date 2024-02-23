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

// ==================== get value from form =================================================
const logBtn = document.getElementById("log-info");
logBtn.addEventListener("click", getvalue);

function getvalue() {
  const inputform = new FormData(document.getElementById("logging-info-form"));
  const form = document.getElementById("logging-info-form");
  // stop timer if it's still running
  if (running) {
    updateStopTimer();
  }
  let setValues = {};
  let items = form.children;
  for (let i = 0; i < items.length; i++) {
    let name = items[i].querySelector("h3");
    setValues[name.textContent] = {};
    let lis = items[i].querySelectorAll("li");
    lis.forEach((li) => {
      const set = li.getAttribute("data-set-id");
      setValues[name.textContent][set] = {};

      const inputs = li.querySelectorAll("input");
      inputs.forEach((input) => {
        setValues[name.textContent][set][input.name] = input.value;
      });
    });
  }
  sendLog(setValues);
}

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

function startExercise() {}
function convertToKG(lb) {
  // for an approximate result, divide the mass value by 2.205
  return parseInt(lb) / 2.205;
}
function convertToKM(miles) {
  // for an approximate result, multiply the length value by 1.609
  return parseInt(miles) * 1.609;
}
