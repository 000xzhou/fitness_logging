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

const popup = document.querySelector(".popup-container");
const overlay = document.getElementById("overlay");

function openupScheduleOptions() {
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
function saveToSchedule(event) {}
