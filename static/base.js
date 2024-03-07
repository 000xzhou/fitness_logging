const myNavLinks = document.getElementById("myNavLinks");
const navIconBtn = document.querySelector(".navIconBtn");
const navIconBtnClose = document.querySelector(".navIconBtnClose");

navIconBtn.addEventListener("click", () => {
  if (myNavLinks.style.display === "block") {
    myNavLinks.style.display = "none";
  } else {
    myNavLinks.style.display = "block";
  }
});
navIconBtnClose.addEventListener("click", () => {
  if (myNavLinks.style.display === "block") {
    myNavLinks.style.display = "none";
  } else {
    myNavLinks.style.display = "block";
  }
});
