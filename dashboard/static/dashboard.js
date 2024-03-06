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
// fetch("/dashboard/graphOfProgress")
//   .then((response) => {
//     if (!response.ok) {
//       throw new Error("Network response was not ok");
//     }
//     return response.text();
//   })
//   .then((data) => {
//     component2.innerHTML = data;
//     lineGraph();
//   })
//   .catch((error) => {
//     console.error("There was a problem with the fetch operation:", error);
//   });

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

function circleGraph() {
  const ctx = document.getElementById("pieGraph");
  fetch("/dashboard/chartofOveralls/data")
    .then(function (response) {
      return response.json();
    })
    .then((data) => {
      if (Object.keys(data).length === 0) {
        console.log("no data found");
      } else {
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
      }
    });
}

// function lineGraph() {
//   const ctx = document.getElementById("graphOfProgress");
//   fetch("/dashboard/graphOfProgress/data")
//     .then(function (response) {
//       return response.json();
//     })
//     .then((data) => {
//       let labels = [];
//       let dataSets = [];
//       console.log(data);
//       for (let key in data) {
//         let datasetData = [];
//         for (let date in data[key]) {
//           datasetData.push(data[key][date]);
//           if (!labels.includes(date)) {
//             labels.push(date);
//           }

//           let isDuplicate = dataSets.some((dataset) => dataset.label === key);
//           if (!isDuplicate) {
//             dataSets.push({
//               label: key,
//               data: datasetData,
//               yAxisID: "y",
//             });
//           }
//         }
//       }
// console.log("labels", labels);
// console.log("dataInsideData", dataInsideData);
// console.log("dataSetName", dataSetName);
// console.log("dataSets", dataSets);

// let dataSetsss = [
//   { label: "Dataset 1", data: [1, 2, 3, 4], yAxisID: "y" },
//   { label: "Dataset 1", data: [1, 3, 3, 4], yAxisID: "y" },
// ];
//       new Chart(ctx, {
//         type: "line",
//         data: {
//           labels: labels,
//           datasets: dataSets,
//         },
//       });
//     });
// }
