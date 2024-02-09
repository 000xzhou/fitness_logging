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
  fetch("/exercises/filter?" + queryString)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then((data) => {
      const exericesInfo = document.getElementById("exerices_info");
      exericesInfo.innerHTML = data;
    })
    .catch((error) => {
      console.error("There was a problem with the fetch operation:", error);
    });
}
