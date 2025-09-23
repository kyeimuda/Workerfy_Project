function moveToNextPage(event) {
    const element = event.target;
    const id = element.id;
    const currentPage = document.querySelector("." + id);
    if (currentPage.className === id) {
    currentPage.style.display = "none";
    };
};

function skip(event) {
    const elemment = event.target;
    document.querySelector(".firstOnboardingPage").style.display = "none";
    document.querySelector(".secondOnboardingPage").style.display = "none"; 
    document.querySelector(".ThirdOnboardingPage").style.display = "none";
    document.querySelector(".fourthOnboardingPage").style.display = "none";
}

document.getElementById('Tdot2').onclick = function () {
    document.querySelector(".secondOnboardingPage").style.display = "flex";
}

document.getElementById('Sdot1').onclick = function () {
    document.querySelector(".firstOnboardingPage").style.display = "flex";
}

document.getElementById('Ftdot3').onclick = function () {
    document.querySelector('.ThirdOnboardingPage').style.display = "flex"
}

