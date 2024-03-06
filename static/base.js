const myNavLinks = document.getElementById("myNavLinks");
const navIconBtn = document.querySelector(".navIconBtn");

navIconBtn.addEventListener("click", () => {
  if (myNavLinks.style.display === "block") {
    myNavLinks.style.display = "none";
  } else {
    myNavLinks.style.display = "block";
  }
});
