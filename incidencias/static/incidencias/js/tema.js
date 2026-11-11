(function () {
  const clave = "oti-tema";
  const raiz = document.documentElement;

  function leer() {
    try {
      return localStorage.getItem(clave);
    } catch (error) {
      return null;
    }
  }

  function guardar(valor) {
    try {
      localStorage.setItem(clave, valor);
    } catch (error) {
      return;
    }
  }

  raiz.setAttribute("data-theme", leer() || "dark");

  document.addEventListener("DOMContentLoaded", function () {
    const botones = document.querySelectorAll("[data-alternar-tema]");
    const meta = document.querySelector('meta[name="theme-color"]');

    function aplicar(valor) {
      raiz.setAttribute("data-theme", valor);
      guardar(valor);
      if (meta) {
        meta.setAttribute("content", valor === "dark" ? "#1e1e1e" : "#d6d6d5");
      }
      botones.forEach(function (boton) {
        boton.setAttribute("aria-pressed", String(valor === "light"));
      });
    }

    aplicar(raiz.getAttribute("data-theme"));

    botones.forEach(function (boton) {
      boton.addEventListener("click", function () {
        aplicar(raiz.getAttribute("data-theme") === "dark" ? "light" : "dark");
      });
    });
  });
})();