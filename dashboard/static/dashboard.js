const component1 = document.getElementById("component1");
const component2 = document.getElementById("component2");
const component3 = document.getElementById("component3");

// Getting the recent workout and displaying it
fetch("/dashboard/recent_workouts")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.text();
  })
  .then((data) => {
    component1.innerHTML = data;
  })
  .catch((error) => {
    console.error("There was a problem with the fetch operation:", error);
  });

// Getting the graphOfProgress and displaying it
fetch("/dashboard/graphOfProgress")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.text();
  })
  .then((data) => {
    component2.innerHTML = data;
  })
  .catch((error) => {
    console.error("There was a problem with the fetch operation:", error);
  });

// Getting the chartofOveralls and displaying it
fetch("/dashboard/chartofOveralls")
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.text();
  })
  .then((data) => {
    component3.innerHTML = data;
    circleGraph();
  })
  .catch((error) => {
    console.error("There was a problem with the fetch operation:", error);
  });

function circleGraph(data) {
  const ctx = document.getElementById("myChart");
  fetch("/dashboard/chartofOveralls/data")
    .then(function (response) {
      return response.json();
    })
    .then((data) => {
      let labelsData = Object.keys(data);
      let dataData = Object.values(data);

      new Chart(ctx, {
        type: "pie",
        data: {
          labels: labelsData,
          datasets: [
            {
              label: "exerice times",
              data: dataData,
              borderWidth: 1,
            },
          ],
        },
      });
    });
}
