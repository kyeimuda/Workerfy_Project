/* Opening and closing the add Past Job PopUp */

document.getElementById("ID_add_job").addEventListener("click", function() {
    document.getElementById("jobAddPopUp").style.display = "block";
});

document.getElementById("ID_close_job").addEventListener("click", function() {   
    document.getElementById("jobAddPopUp").style.display = "none";
})


/* Openning and Closing the Add School PopUp */
document.getElementById("ID_add_school").addEventListener("click", function() {
    document.getElementById("SchoolAddPopUp").style.display = "block";
});

document.getElementById("ID_close_school").addEventListener("click", function() {   
    document.getElementById("SchoolAddPopUp").style.display = "none";
})

/* Openning and Closing the Add Cert PopUp */
document.getElementById("ID_add_cert").addEventListener("click", function() {
    document.getElementById("certAddPopUp").style.display = "block";
});

document.getElementById("ID_close_cert").addEventListener("click", function() {   
    document.getElementById("certAddPopUp").style.display = "none";
})

/* Openning and Closing the Add Portfolio item PopUp */
document.getElementById("ID_add_portfolio").addEventListener("click", function() {
    document.getElementById("portAddPopUp").style.display = "block";
});

document.getElementById("ID_close_Portfolio").addEventListener("click", function() {   
    document.getElementById("portAddPopUp").style.display = "none";
})
