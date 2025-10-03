/* Opening and closing the add Past Job PopUp */

document.getElementById("ID_add_job").addEventListener("click", function() {
    document.getElementById("jobAddPopUp").style.display = "block";
});

document.getElementById("ID_close_job").addEventListener("click", function() {  
    const year = document.getElementById("date").value;
    const organization = document.getElementById("Organization_Or_Title").value;
    const roleOrDescription = document.getElementById("discription").value;

    data = '{"Year": "'+ year + '", "Organization": "' + organization + '", "role": "' + roleOrDescription + '"}'

    const Input = document.getElementById('Working_Areas');

    if (!Input.value) {
    
        Input.value = data;

    } else {
        Input.value += "-- " + data;


    }

    document.getElementById("date").value = '';
    document.getElementById("Organization_Or_Title").value = '';
    document.getElementById("discription").value = '';
 
    document.getElementById("jobAddPopUp").style.display = "none";
})


/* Openning and Closing the Add School PopUp */
document.getElementById("ID_add_school").addEventListener("click", function() {
    document.getElementById("SchoolAddPopUp").style.display = "block";
});

document.getElementById("ID_close_school").addEventListener("click", function() {
    
    const institution_or_school = document.getElementById("institution_or_school").value;
    const school_date = document.getElementById("school_date").value;
    const schoolLevel = document.getElementById("schoolLevel").value;
    alert(institution_or_school)

    data = '{"institution_or_school": "'+ institution_or_school + '", "school_date": "' + school_date + '", "schoolLevel": "' + schoolLevel + '"}'
    alert(data)

    const Input = document.getElementById('Education_Schools');
    alert(Input.value)

    if (!Input.value) {
    
        Input.value = data;
        alert(Input.value)
    } else {
        Input.value += "-- " + data;


    }

    document.getElementById("institution_or_school").value = '';
    document.getElementById("school_date").value = '';
    document.getElementById("schoolLevel").value = '';

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

//Getting the social links input
links = document.getElementsByClassName("slinks");


function addValue(links) {
    for (i of links) {
        i.addEventListener("change", function(event) {

            if (!document.getElementById('Social_Links').value) {
                inputLinks = {};
                if (event.target.value) {
                    linkName = event.target.name;
                    linkValue = event.target.value;

                    if (linkName === "facebook") {
                        inputLinks.facebook = linkValue
                    } else if (linkName === "twitter"){
                        inputLinks.twitter = linkValue
                    } else if (linkName === "instagram") {
                        inputLinks.instagram = linkValue
                    } else if (linkName === "tiktok"){
                        inputLinks.tiktok = linkValue
                    }
                }

                document.getElementById('Social_Links').value = JSON.stringify(inputLinks, null)
            } else {
    

                inputLinks = JSON.parse(document.getElementById('Social_Links').value);
                if (event.target.value) {
                    linkName = event.target.name;
                    linkValue = event.target.value;

                    if (linkName === "facebook") {
                        inputLinks.facebook = linkValue
                    } else if (linkName === "twitter"){
                        inputLinks.twitter = linkValue
                    } else if (linkName === "instagram") {
                        inputLinks.instagram = linkValue
                    } else if (linkName === "tiktok"){
                        inputLinks.tiktok = linkValue
                    }
                }

                document.getElementById('Social_Links').value = JSON.stringify(inputLinks, null)

            }
});
}
};

addValue(links);


// This is for Getting the value of the specility field

/* document.getElementById('add_speciality_BTN').addEventListener("click", function() {

    inputValue = document.getElementById('Speciality_input').value;
    inputField = document.getElementById("Trade_Specialties");

    if (inputValue) {
        inputField.value += inputValue + " ";
    }

    document.getElementById('Speciality_input').value = "";
   
}); */

function addAbility(inputValue, inputField) {
    inputcontainer = inputValue;
    inputValue = inputValue.value;
    inputField = inputField;


    if (inputValue) {
        inputField.value += inputValue + ",";
    }

    inputcontainer.value = "";
}

document.getElementById('add_speciality_BTN').addEventListener('click', function() {
    addAbility(document.getElementById('Speciality_input'), document.getElementById("Trade_Specialties"))
}
);

document.getElementById('add_skill_BTN').addEventListener('click', function() {
    addAbility(document.getElementById('Skills_input'), document.getElementById("Skills"))
}
);

document.getElementById('add_otherskill_BTN').addEventListener('click', function() {
    addAbility(document.getElementById('Other_Skills_input'), document.getElementById("OtherSkills"))
}
);

// This is for the cancel button pop up
document.getElementById('CancelBTNmain').addEventListener('click', function() {
    document.getElementById('CancelPopUp').style.display = 'flex';
});

document.getElementById('CancelPopUp').addEventListener('click', function(event) {
    if (event.target === document.getElementById('CancelPopUp')) {
        document.getElementById('CancelPopUp').style.display = 'none';
    }
    
});

document.getElementById('ContinueEditing').addEventListener('click', function() {
    document.getElementById('CancelPopUp').style.display = 'none';
});

document.getElementById('StillCancel').addEventListener('click', function() {
    document.location.href = "http://localhost:8000/main/Main";
});


