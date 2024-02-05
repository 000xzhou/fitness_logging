const popupContainer = document.getElementById("popupContainer");
const editBtn = document.querySelectorAll(".edit-btn");
const deleteBtn = document.querySelectorAll(".delete-btn");

deleteBtn.forEach((btn) => btn.addEventListener("click", deleteSchedule));

function deleteSchedule(e) {
  let parentElement = e.target.parentElement;
  const scheduleId = {
    id: parentElement.id,
  };
  fetch("/schedule/delete_schedule", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(scheduleId),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      if (data.message == "Schedule deleted successfully") {
        parentElement.remove();
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
