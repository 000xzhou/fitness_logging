const equipment = document.getElementById("equipment");
const muscles = document.getElementById("muscles");

// Getting the recent workout and displaying it
fetch("/exercises/muscles")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.text();
  })
  .then((data) => {
    muscles.innerHTML = data;
  })
  .catch((error) => {
    console.error("There was a problem with the fetch operation:", error);
  });

// Getting the graphOfProgress and displaying it
fetch("/exercises/equipment")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.text();
  })
  .then((data) => {
    equipment.innerHTML = data;
  })
  .catch((error) => {
    console.error("There was a problem with the fetch operation:", error);
  });

fetch("/exercises/filter")
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
