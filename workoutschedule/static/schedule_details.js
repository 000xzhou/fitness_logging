const searchForm = document.getElementById("search-form");
const exercises = document.getElementById("exercises");
const searchTerm = document.getElementById("search-term");

searchTerm.addEventListener("input", searchExercises);
searchForm.addEventListener("submit", searchExercises);

function searchExercises(e) {
  e.preventDefault();
  fetch(`/exercises/search?term=${searchTerm.value}`, {
    method: "get",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.text();
    })
    .then((data) => {
      exercises.innerHTML = data;
      //   console.log(data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
