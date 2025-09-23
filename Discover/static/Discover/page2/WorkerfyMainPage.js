document.querySelectorAll(".navlist li").forEach(nav => {
    nav.addEventListener("click", (e) => {
        document.querySelectorAll(".navlist li").forEach(n => n.classList.remove("activeNav"));
        e.currentTarget.classList.add("activeNav");
        })
    });
