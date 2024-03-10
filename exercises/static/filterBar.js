function filterExerices() {
  // console.log(event.target);
  const selectEquipment = document.getElementById("select_equipment");
  const selectMuscle = document.getElementById("select_muscle");

  // Get the selected values
  const selectedEquipment = selectEquipment.value;
  const selectedMuscle = selectMuscle.value;

  const selectedValues = {
    equipment: selectedEquipment,
    muscle: selectedMuscle,
  };
  const queryString = new URLSearchParams(selectedValues).toString();
  fetchData(queryString);
}

function fetchData(queryString) {
  fetch("/exercises/filter?" + queryString)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then((data) => {
      const exericesInfo = document.getElementById("exerices_info");
      exericesInfo.insertAdjacentHTML("beforeend", data);
      // exericesInfo.innerHTML = data;
    })
    .catch((error) => {
      console.error("There was a problem with the fetch operation:", error);
    });
}

// load more ==============>
let count = 0;
window.onscroll = function (ev) {
  if (
    window.innerHeight + Math.round(window.scrollY) >=
    document.body.offsetHeight
  ) {
    // you're at the bottom of the page
    const selectEquipment = document.getElementById("select_equipment");
    const selectMuscle = document.getElementById("select_muscle");

    const selectedEquipment = selectEquipment.value;
    const selectedMuscle = selectMuscle.value;
    count++;
    const selectedValues = {
      equipment: selectedEquipment,
      muscle: selectedMuscle,
      offset: count * 21,
    };
    const queryString = new URLSearchParams(selectedValues).toString();
    fetchData(queryString);
  }
};

//=============================== pop ups and checkboxes ====================================
const popup = document.querySelector(".popup-container");
const overlay = document.getElementById("overlay");
const checkboxes = document.querySelectorAll('[name="workout_plan_ids"]');

function openupScheduleOptions(event) {
  let siblingDiv = event.target.previousElementSibling;
  let name = siblingDiv.querySelector("h3");
  let id = name.getAttribute("data-exercise-id");
  popup.setAttribute("data-name", name.textContent);
  popup.setAttribute("data-name-id", id);
  let exericename = popup.getAttribute("data-name");
  checkboxes.forEach((checkbox) => {
    let planid = checkbox.id;
    // start ===
    fetch("/schedule/checkInSchedule", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        exericename: exericename,
        planid: planid,
      }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        if (data.success) {
          console.log("Success:", data.message);
          checkbox.checked = true;
          checkbox.setAttribute("exerciseInPlan-id", data.message);
        } else {
          console.log("Failure:", data.message);
          checkbox.checked = false;
        }
      })
      .catch((error) => console.error("Error:", error));
    // end ===
  });

  if ((popup.style.display = "none")) {
    popup.style.display = "block";
    overlay.style.display = "block";
  } else {
    popup.style.display = "none";
    overlay.style.display = "none";
  }
}
overlay.addEventListener("click", function () {
  popup.style.display = "none";
  overlay.style.display = "none";
});

checkboxes.forEach((checkbox) =>
  checkbox.addEventListener("change", function () {
    let ischecked = checkbox.checked;
    if (ischecked) {
      let workoutPlanId = checkbox.id;
      let name = popup.getAttribute("data-name");
      let exercise_id = popup.getAttribute("data-name-id");
      addtoschedule(name, exercise_id, workoutPlanId);
    } else {
      let exerciseInPlanId = checkbox.getAttribute("exerciseInPlan-id");
      removefromschedule(exerciseInPlanId);
    }
  })
);
function addtoschedule(name, exercise_id, workoutPlanId) {
  fetch("/schedule/addExericeToSchedule", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      workoutPlanId: workoutPlanId,
      name: name,
      exercise_id: exercise_id,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data.message);
      // let numbers = data.message.match(/\d+/);
      // popup.setAttribute("data-exerciseInPlan-id", numbers);
    })
    .catch((error) => console.error("Error:", error));
}
function removefromschedule(exerciseInPlanId) {
  fetch("/schedule/removeExericeToSchedule", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      exerciseInPlanId: exerciseInPlanId,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data.message);
    })
    .catch((error) => console.error("Error:", error));
}

function checkInSchedule(exericename, planid) {
  fetch("/schedule/checkInSchedule", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      exericename: exericename,
      planid: planid,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      if (data.success) {
        console.log("Success:", data.message);
        ans = true;
      } else {
        console.log("Failure:", data.message);
        ans = false;
      }
    })
    .catch((error) => console.error("Error:", error));
}
