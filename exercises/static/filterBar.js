const equipment = document.getElementById("equipment");
const muscles = document.getElementById("muscles");
// const component3 = document.getElementById("component3");

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

// Getting the chartofOveralls and displaying it
// fetch("/dashboard/chartofOveralls")
//   .then((response) => {
//     if (!response.ok) {
//       throw new Error("Network response was not ok");
//     }
//     return response.text();
//   })
//   .then((data) => {
//     component3.innerHTML = data;
//   })
//   .catch((error) => {
//     console.error("There was a problem with the fetch operation:", error);
//   });
