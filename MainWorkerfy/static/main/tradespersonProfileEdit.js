/* Opening and closing the add Past Job PopUp */

const addJobBtn = document.getElementById("ID_add_job");
if (addJobBtn) {
    addJobBtn.addEventListener("click", function() {
        document.getElementById("jobAddPopUp").style.display = "block";
    });
}

const closeJobBtn = document.getElementById("ID_close_job");
if (closeJobBtn) {
    closeJobBtn.addEventListener("click", function() {  
        const year = document.getElementById("date").value;
        const organization = document.getElementById("Organization_Or_Title").value;
        const roleOrDescription = document.getElementById("discription").value;

        data = '{"Year": "'+ year + '", "Organization": "' + organization + '", "role": "' + roleOrDescription + '"}'

        const Input = document.getElementById('Working_Areas');

        if (Input) {
            if (!Input.value) {
            
                Input.value = data;

            } else {
                Input.value += "-- " + data;
            }
        }

        document.getElementById("date").value = '';
        document.getElementById("Organization_Or_Title").value = '';
        document.getElementById("discription").value = '';
     
        document.getElementById("jobAddPopUp").style.display = "none";
    });
}


/* Openning and Closing the Add School PopUp */
const addSchoolBtn = document.getElementById("ID_add_school");
if (addSchoolBtn) {
    addSchoolBtn.addEventListener("click", function() {
        document.getElementById("SchoolAddPopUp").style.display = "block";
    });
}

const closeSchoolBtn = document.getElementById("ID_close_school");
if (closeSchoolBtn) {
    closeSchoolBtn.addEventListener("click", function() {
        
        const institution_or_school = document.getElementById("institution_or_school").value;
        const school_date = document.getElementById("school_date").value;
        const schoolLevel = document.getElementById("schoolLevel").value;

        data = {};
        dataArray = [];

        /* data = '{"institution_or_school": "'+ institution_or_school + '", "school_date": "' + school_date + '", "schoolLevel": "' + schoolLevel + '"}' */
        data.institution_or_school = institution_or_school;
        data.school_date = school_date;
        data.schoolLevel = schoolLevel;

        dataArray.push(data)


        alert(JSON.stringify(data))
        alert(JSON.stringify(dataArray))

        const Input = document.getElementById('Education_Schools');
        alert(Input ? Input.value : 'Input not found')

        if (Input) {
            if (!Input.value) {
            
                Input.value = JSON.stringify(dataArray);
                alert(Input.value)
            } else {
                retrivedData = JSON.parse(Input.value);
                retrivedData.push(data);
                Input.value = JSON.stringify(retrivedData);
            }
        }

        document.getElementById("institution_or_school").value = '';
        document.getElementById("school_date").value = '';
        document.getElementById("schoolLevel").value = '';

        document.getElementById("SchoolAddPopUp").style.display = "none";
    });
}

/* Openning and Closing the Add Cert PopUp */
const addCertBtn = document.getElementById("ID_add_cert");
if (addCertBtn) {
    addCertBtn.addEventListener("click", function() {
        document.getElementById("certAddPopUp").style.display = "block";
    });
}

const closeCertBtn = document.getElementById("ID_close_cert");
if (closeCertBtn) {
    closeCertBtn.addEventListener("click", function() {   
        document.getElementById("certAddPopUp").style.display = "none";
    });
}

/* Openning and Closing the Add Portfolio item PopUp */
const addPortfolioBtn = document.getElementById("ID_add_portfolio");
if (addPortfolioBtn) {
    addPortfolioBtn.addEventListener("click", function() {
        document.getElementById("portAddPopUp").style.display = "block";
    });
}

const closePortfolioBtn = document.getElementById("ID_close_Portfolio");
if (closePortfolioBtn) {
    closePortfolioBtn.addEventListener("click", function() {   
        document.getElementById("portAddPopUp").style.display = "none";
    });
}

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

    if (inputField.value) {
        prevData = JSON.parse(inputField.value);
        prevData.push(inputValue);
        inputField.value = JSON.stringify(prevData);
    } else {
        data = []; data.push(inputValue);
        inputField.value = JSON.stringify(data);
        alert(data);
        alert(inputField.value);
    }

    if (inputcontainer) {
        inputcontainer.value = "";
    }
}

const addSpecialityBtn = document.getElementById('add_speciality_BTN');
if (addSpecialityBtn) {
    addSpecialityBtn.addEventListener('click', function() {
        addAbility(document.getElementById('Speciality_input'), document.getElementById("Trade_Specialties"))
    });
}

const addSkillBtn = document.getElementById('add_skill_BTN');
if (addSkillBtn) {
    addSkillBtn.addEventListener('click', function() {
        addAbility(document.getElementById('Skills_input'), document.getElementById("Skills"))
    });
}

const addOtherSkillBtn = document.getElementById('add_otherskill_BTN');
if (addOtherSkillBtn) {
    addOtherSkillBtn.addEventListener('click', function() {
        addAbility(document.getElementById('Other_Skills_input'), document.getElementById("OtherSkills"))
    });
}

// This is for the cancel button pop up
const cancelBtn = document.getElementById('CancelBTNmain');
if (cancelBtn) {
    cancelBtn.addEventListener('click', function() {
        document.getElementById('CancelPopUp').style.display = 'flex';
    });
}

const cancelPopup = document.getElementById('CancelPopUp');
if (cancelPopup) {
    cancelPopup.addEventListener('click', function(event) {
        if (event.target === document.getElementById('CancelPopUp')) {
            document.getElementById('CancelPopUp').style.display = 'none';
        }
        
    });
}

const continueEditingBtn = document.getElementById('ContinueEditing');
if (continueEditingBtn) {
    continueEditingBtn.addEventListener('click', function() {
        document.getElementById('CancelPopUp').style.display = 'none';
    });
}

const stillCancelBtn = document.getElementById('StillCancel');
if (stillCancelBtn) {
    stillCancelBtn.addEventListener('click', function() {
        document.location.href = "http://localhost:8000/main/Main";
    });
}


