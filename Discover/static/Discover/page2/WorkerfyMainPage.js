document.querySelectorAll(".navlist li").forEach(nav => {
    nav.addEventListener("click", (e) => {
        document.querySelectorAll(".navlist li").forEach(n => n.classList.remove("activeNav"));
        e.currentTarget.classList.add("activeNav");
        })
    });


document.getElementById("editProfileButton").addEventListener("click", () => {
    window.location.href = "/main/EditTradesperson";
});

document.getElementById("WorkNavControl_id").addEventListener("click", function() {
    const element = document.getElementById('WorkSideNav_id');
    const list = Array.from(element.classList);
    
    if (list.includes("navOpen")) {
        element.classList.remove("navOpen");
        element.classList.add("navClose"); 
    } else {
        element.classList.remove("navClose");
        element.classList.add("navOpen"); 
    }
});



