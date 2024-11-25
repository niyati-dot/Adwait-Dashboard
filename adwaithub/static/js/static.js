
// Message/Notification timer
//devices.html js
document.querySelectorAll(".sidebar-link").forEach((link) => {
  if (link.href === window.location.href) {
      link.classList.add("active");
      link.setAttribute("aria-current", "page");
  }
});

document.addEventListener("DOMContentLoaded", function() {
  let message_timeout = document.getElementById("message-timer");
  if (message_timeout) {
    setTimeout(function() {
      message_timeout.style.display = "none";
    }, 5000);
  }

  let message_alert_timeout = document.getElementById("message-alert");
  if (message_alert_timeout) {
    setTimeout(function() {
      message_alert_timeout.style.display = "none";
    }, 5000);
  }

});