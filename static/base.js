const myNavLinks = document.getElementById("myNavLinks");
const navIconBtn = document.querySelector(".navIconBtn");
const navIconBtnClose = document.querySelector(".navIconBtnClose");
const menu = document.querySelector(".material-symbols-outlined");

navIconBtn.addEventListener("click", () => {
  if (myNavLinks.style.display === "block") {
    myNavLinks.style.display = "none";
    menu.textContent = "menu";
  } else {
    myNavLinks.style.display = "block";
    menu.textContent = "close";
  }
});
