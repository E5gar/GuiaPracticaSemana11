(function () {
  const panel = document.getElementById("panel-comandos");

  if (panel) {
    const input = panel.querySelector(".cmd__input");
    const items = Array.from(panel.querySelectorAll(".cmd__item"));
    const vacio = panel.querySelector(".cmd__vacio");
    let activo = 0;
    let previo = null;
    let navegado = false;

    function visibles() {
      return items.filter(function (item) {
        return !item.parentElement.hidden;
      });
    }

    function marcar(indice) {
      const lista = visibles();
      items.forEach(function (item) {
        item.classList.remove("is-activo");
      });
      if (lista.length === 0) {
        activo = 0;
        return;
      }
      activo = (indice + lista.length) % lista.length;
      lista[activo].classList.add("is-activo");
      lista[activo].scrollIntoView({ block: "nearest" });
    }

    function filtrar(texto) {
      const consulta = texto.trim().toLowerCase();
      items.forEach(function (item) {
        const coincide =
          consulta === "" || item.dataset.texto.toLowerCase().includes(consulta);
        item.parentElement.hidden = !coincide;
      });
      vacio.hidden = visibles().length > 0;
      navegado = false;
      marcar(0);
    }

    function abrir() {
      previo = document.activeElement;
      panel.hidden = false;
      document.body.classList.add("sin-scroll");
      input.value = "";
      filtrar("");
      input.focus();
    }

    function cerrar() {
      panel.hidden = true;
      document.body.classList.remove("sin-scroll");
      if (previo && typeof previo.focus === "function") {
        previo.focus();
      }
    }

    document.querySelectorAll("[data-abrir-comandos]").forEach(function (boton) {
      boton.addEventListener("click", abrir);
    });

    panel.querySelectorAll("[data-cerrar-comandos]").forEach(function (zona) {
      zona.addEventListener("click", cerrar);
    });

    input.addEventListener("input", function () {
      filtrar(input.value);
    });

    input.addEventListener("keydown", function (evento) {
      if (evento.key === "ArrowDown") {
        evento.preventDefault();
        navegado = true;
        marcar(activo + 1);
      } else if (evento.key === "ArrowUp") {
        evento.preventDefault();
        navegado = true;
        marcar(activo - 1);
      } else if (evento.key === "Enter" && navegado) {
        const lista = visibles();
        if (lista[activo]) {
          evento.preventDefault();
          lista[activo].click();
        }
      }
    });

    document.addEventListener("keydown", function (evento) {
      const atajo = (evento.ctrlKey || evento.metaKey) && evento.key.toLowerCase() === "k";
      if (atajo) {
        evento.preventDefault();
        if (panel.hidden) {
          abrir();
        } else {
          cerrar();
        }
      } else if (evento.key === "Escape" && !panel.hidden) {
        cerrar();
      }
    });
  }

  if (window.lucide) {
    window.lucide.createIcons();
  }
})();