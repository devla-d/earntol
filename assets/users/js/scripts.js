const togglebar = document.getElementById("togglebar");
const sidebar = document.getElementById("dsidebar");
var togglebar_active = false;
togglebar.addEventListener("click", () => {
  if (!togglebar_active) {
    sidebar.classList.add("toggled");
    togglebar_active = true;
  } else {
    sidebar.classList.remove("toggled");
    togglebar_active = false;
  }
  console.log(togglebar_active);
});
