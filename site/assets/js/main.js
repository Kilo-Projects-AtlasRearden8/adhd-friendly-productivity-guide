/* Low-Energy Productivity — site behavior */

(function () {
  "use strict";

  // Mobile menu toggle
  var btn = document.querySelector(".menu-btn");
  var root = document.documentElement;

  if (btn) {
    btn.addEventListener("click", function () {
      var open = root.classList.toggle("menu-open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // Close menu when a nav link is clicked
  var links = document.querySelectorAll(".nav a");
  links.forEach(function (link) {
    link.addEventListener("click", function () {
      root.classList.remove("menu-open");
      if (btn) btn.setAttribute("aria-expanded", "false");
    });
  });

  // Announce print tip on worksheet pages (non-intrusive)
  var hint = document.getElementById("print-hint");
  if (hint) {
    hint.textContent = "Tip: use File → Print (Ctrl+P / Cmd+P) to print this worksheet.";
  }
})();
