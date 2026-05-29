/* Opening and closing the add Past Job PopUp */
const ID_add_WorkExperience = document.getElementById("ID_add_WorkExperience");
if (ID_add_WorkExperience) {
    ID_add_WorkExperience.addEventListener("click", function() {
        document.getElementById("WorkExperienceAddPopUp").style.display = "block";
    });
}

const ID_close_WorkExperience = document.getElementById("ID_close_experience");
if (ID_close_WorkExperience) {
    ID_close_experience.addEventListener("click", function() {
        document.getElementById("WorkExperienceAddPopUp").style.display = "none";
    })
};

const add_Experience = document.getElementById("ID_add_experience");
if (add_Experience) {
    add_Experience.addEventListener("click", function() {  
        const Role = document.getElementById("RoleID").value;
        const Date = document.getElementById("Experience_dateID").value;
        const Discription = document.getElementById("DiscriptionID").value;

        data = {};
        dataArray = [];

        data.Role = Role;
        data.Date = Date;
        data.Discription = Discription;

        dataArray.push(data)

        alert(JSON.stringify(data))
        alert(JSON.stringify(dataArray))

        const Input = document.getElementById('Work_Experience');

        if (Input && (Role || Date || Discription)) {
            if (!Input.value) {
            
                Input.value = JSON.stringify(dataArray);
                alert(Input.value)
                document.getElementById("RoleID").value = '';
                document.getElementById("Experience_dateID").value = '';
                document.getElementById("DiscriptionID").value = '';
            } else {
                retrivedData = JSON.parse(Input.value);
                retrivedData.push(data);
                Input.value = JSON.stringify(retrivedData);
                document.getElementById("RoleID").value = '';
                document.getElementById("Experience_dateID").value = '';
                document.getElementById("DiscriptionID").value = '';
            }
        }
        document.getElementById("WorkExperienceAddPopUp").style.display = "none";
    });
}


/* Openning and Closing the Add School PopUp */
const addSchoolBtn = document.getElementById("ID_add_school");
if (addSchoolBtn) {
    addSchoolBtn.addEventListener("click", function() {
        document.getElementById("SchoolAddPopUp").style.display = "block";
    });
}

const closeSchoolPopUP = document.getElementById('ID_close_schoolPopUp');
if (closeSchoolPopUP) {
    closeSchoolPopUP.addEventListener("click", function() {
        document.getElementById("SchoolAddPopUp").style.display = "none";
    })

}

const closeSchoolBtn = document.getElementById("ID_add_schoolpopUp");
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

        if (Input && (institution_or_school || school_date || schoolLevel)) {
            if (!Input.value) {
            
                Input.value = JSON.stringify(dataArray);
                alert(Input.value)
                document.getElementById("institution_or_school").value = '';
                document.getElementById("school_date").value = '';
                document.getElementById("schoolLevel").value = '';
            } else {
                retrivedData = JSON.parse(Input.value);
                retrivedData.push(data);
                Input.value = JSON.stringify(retrivedData);
                document.getElementById("institution_or_school").value = '';
                document.getElementById("school_date").value = '';
                document.getElementById("schoolLevel").value = '';
            }
        }
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

// This is for the contact number field to add the country code to the number
const contactField = document.getElementById("PhoneClone");
if (contactField) {
    contactField.addEventListener("change", function() {
        countryCode = document.getElementById("countryCode").value;
        alert("heree " + countryCode)
        document.getElementById("Phone1").value = countryCode + this.value.l;
    });
};

const contactField2 = document.getElementById("PhoneClone2");
if (contactField2) {
    contactField2.addEventListener("change", function() {
        countryCode = document.getElementById("countryCode2").value;
        document.getElementById("Phone2").value = countryCode +this.value;
    });
};

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
    }

    if (inputcontainer) {
        inputcontainer.value = "";
    }
}

const addSpecialityBtn = document.getElementById('add_speciality_BTN');
if (addSpecialityBtn) {
    addSpecialityBtn.addEventListener('click', function() {
        addAbility(document.getElementById('Speciality_input'), document.getElementById("Trade_Specialties"))
        console.log(document.getElementById("Trade_Specialties").value)
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

// Handle form submit to send PUT request to API
const form = document.getElementById('form');
if (form) {
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const submitButton = form.querySelector('[type="submit"]');
        const userId = this.dataset.userId;
        const formData = new FormData();
        const inputs = form.querySelectorAll('input[class|="inputField"], select[class|="inputField"], textarea[class|="inputField"]');
        inputs.forEach(input => {
            if(input.name === 'csrfmiddlewaretoken') {
                return;
            } else if (input.type === 'file') {
                if (input.files.length > 0) {
                    formData.append(input.name, input.files[0]);
                }
            } else if (input.value.trim() !== '') {
                formData.append(input.name, input.value);
            }
        });

        // Show loading state
        if (submitButton) {
            submitButton.disabled = true;
            submitButton.dataset.originalText = submitButton.textContent;
            submitButton.textContent = 'Saving…';
        }

        fetch(`/api/v1/tradespeople/${userId}/`, {
            method: 'PATCH',
            body: formData,
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            }
        })
        .then(response => {
            if (response.status === 200) {
                const createdConfirnmation = document.querySelector('.created');
                if (createdConfirnmation) {
                    createdConfirnmation.style.display = 'flex';
                }

                data = response.json();
                console.log('Profile updated successfully');
                console.log('Response:', data); // Debugging line'
                return data;
            }
            console.log('Raw response:', response); // Debugging line
            console.log('Response status:', response.status); // Debugging line
            return "Failed";
        })
        .then(data => {
            if (data == "Failed") {
                console.log('Success:', data);
                // Redirect or show success message
            }
            
        })
        .catch(error => {
            const createdConfirnmation = document.querySelector('.not_create');
            if (createdConfirnmation) {
                    createdConfirnmation.style.display = 'flex';
            };
            console.log('failed')
            console.error('Error:', error);
        })
        .finally(() => {
            // Restore button state
            if (submitButton) {
                submitButton.disabled = false;
                submitButton.textContent = submitButton.dataset.originalText || 'Save';
            }
        });
    });
}

const addAnotherButton = document.getElementById('AddAnother');
if (addAnotherButton) {
    addAnotherButton.addEventListener('click', () => {
        form.reset();
        const createdConfirnmation = document.querySelector('.created');
        if (createdConfirnmation) {
            createdConfirnmation.style.display = 'none';
        }

    }
)}


// This is for the retry button in case of failed update
const re_tryButton = document.getElementById('re_try');
if (re_tryButton) {
    re_tryButton.addEventListener('click', () => {
        form.reset();
        const createdConfirnmation = document.querySelector('.not_create');
        if (createdConfirnmation) {
            createdConfirnmation.style.display = 'none';
        }

    }
)}

// This is for the remove skill

const remove_skill_BTN = document.getElementById('remove_skill_BTN');
if (remove_skill_BTN) {
    remove_skill_BTN.addEventListener('click', function(e) {
        e.target.style.visibility = "hidden";
        document.querySelector(".deleteSkillContainer").style.display = "flex";
    });
}

const cancel_remove_skill_BTN = document.getElementById('cancel_remove_skill_BTN');
if (cancel_remove_skill_BTN) {
    cancel_remove_skill_BTN.addEventListener('click', function(e) {
        document.getElementById('remove_skill_BTN').style.visibility = "visible";
        document.querySelector(".deleteSkillContainer").style.display = "none";
    });
}

document.querySelectorAll(".skillTag").forEach(tag => {
    tag.addEventListener("click", function() {
        if (tag.classList.contains("selected")) {
            tag.classList.remove("selected");
            tag.style.backgroundColor = "#E3D5C0";
        } else {            
            tag.classList.add("selected");
            tag.style.backgroundColor = "gray";
    }
    });
});

const done_remove_skill_BTN = document.getElementById('done_remove_skill_BTN');
if (done_remove_skill_BTN) {
    done_remove_skill_BTN.addEventListener('click', function() {
        const selectedTags = document.querySelectorAll(".skillTag.selected");
        const deletList = [];
        selectedTags.forEach(tag => {
            deletList.push(tag.dataset.skill);
        });
        console.log(deletList);
        document.getElementById('Delete_Skill').value = JSON.stringify(deletList);
        document.getElementById('remove_skill_BTN').style.visibility = "visible";
        document.querySelector(".deleteSkillContainer").style.display = "none";
        console.log(document.getElementById('Delete_Skill').value);
    });
}


// This is for the remove speciality
const remove_speciality_BTN = document.getElementById('remove_speciality_BTN');
if (remove_speciality_BTN) {
    remove_speciality_BTN.addEventListener('click', function(e) {
        e.target.style.visibility = "hidden";
        document.querySelector(".deleteSpecialityContainer").style.display = "flex";
    });
}

const cancel_remove_speciality_BTN = document.getElementById('cancel_remove_speciality_BTN');
if (cancel_remove_speciality_BTN) {
    cancel_remove_speciality_BTN.addEventListener('click', function(e) {
        document.getElementById('remove_speciality_BTN').style.visibility = "visible";
        document.querySelector(".deleteSpecialityContainer").style.display = "none";
    });
}

document.querySelectorAll(".specialityTag").forEach(tag => {
    tag.addEventListener("click", function() {
        if (tag.classList.contains("selected")) {
            tag.classList.remove("selected");
            tag.style.backgroundColor = "#E3D5C0";
        } else {            
            tag.classList.add("selected");
            tag.style.backgroundColor = "gray";
    }
    });
});

const done_remove_speciality_BTN = document.getElementById('done_remove_speciality_BTN');
if (done_remove_speciality_BTN) {
    done_remove_speciality_BTN.addEventListener('click', function() {
        const selectedTags = document.querySelectorAll(".specialityTag.selected");
        const deletList = [];
        selectedTags.forEach(tag => {
            deletList.push(tag.dataset.skill);
        });
        console.log(deletList);
        document.getElementById('Delete_Speciality').value = JSON.stringify(deletList);
        document.getElementById('remove_speciality_BTN').style.visibility = "visible";
        document.querySelector(".deleteSpecialityContainer").style.display = "none";
        console.log(document.getElementById('Delete_Speciality').value);
    });
}

// This is for the remove other Skill
const remove_other_skill_BTN = document.getElementById('remove_otherskill_BTN');
if (remove_other_skill_BTN) {
    remove_other_skill_BTN.addEventListener('click', function(e) {
        e.target.style.visibility = "hidden";
        document.querySelector(".deleteOtherSkillContainer").style.display = "flex";
    });
};

const cancel_remove_other_skill_BTN = document.getElementById('cancel_remove_otherskill_BTN');
if (cancel_remove_other_skill_BTN) {
    cancel_remove_other_skill_BTN.addEventListener('click', function(e) {
        document.getElementById('remove_otherskill_BTN').style.visibility = "visible";
        document.querySelector(".deleteOtherSkillContainer").style.display = "none";
    });
};

document.querySelectorAll(".otherSkillTag").forEach(tag => {
    tag.addEventListener("click", function() {
        if (tag.classList.contains("selected")) {
            tag.classList.remove("selected");
            tag.style.backgroundColor = "#E3D5C0";
        } else {            
            tag.classList.add("selected");
            tag.style.backgroundColor = "gray";
    }
    });
});

const done_remove_other_skill_BTN = document.getElementById('done_remove_otherskill_BTN');
if (done_remove_other_skill_BTN) {
    done_remove_other_skill_BTN.addEventListener('click', function() {
        const selectedTags = document.querySelectorAll(".otherSkillTag.selected");
        const deletList = [];
        selectedTags.forEach(tag => {
            deletList.push(tag.dataset.skill);
        });
        console.log(deletList);
        document.getElementById('Delete_Other_Skill').value = JSON.stringify(deletList);
        document.getElementById('remove_otherskill_BTN').style.visibility = "visible";
        document.querySelector(".deleteOtherSkillContainer").style.display = "none";
        console.log(document.getElementById('Delete_Other_Skill').value);
    });
}

