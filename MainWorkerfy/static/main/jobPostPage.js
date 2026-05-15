document.getElementById("CancelBTNmain").addEventListener("click", () => {
    document.getElementById("CancelPopUp").style.display = "flex";
})

document.getElementById("ContinueEditing").addEventListener("click", () => {
    document.getElementById("CancelPopUp").style.display = "none";
})

document.getElementById("fromAmount").addEventListener("change", function(event) {
    Budget_Range = document.getElementById("Budget_Range");
    if (event.target.value) {
        Budget_Range.value = event.target.value;
    };
})

document.getElementById("toAmount").addEventListener("change", (event) => {
    Budget_Range = document.getElementById("Budget_Range");
    if (event.target.value) {
        Budget_Range.value += "-" + event.target.value;
    };
});


function addAbility(inputValue, inputField) {
    inputcontainer = inputValue;
    inputValue = inputValue.value;
    inputField = inputField;


    if (inputValue) {
        inputField.value += inputValue + ",";

        const tagHolder = document.getElementById('TagHolder');

        const newTag = document.createElement('p');
        newTag.textContent = inputValue;
        newTag.classList.add('Tags');
        
        tagHolder.appendChild(newTag);
        }

    inputcontainer.value = "";
    
}



document.getElementById('addBTN_id').addEventListener('click', function () {
    addAbility(document.getElementById('skill_tags_id'), document.getElementById("Required_Skills"))
});

document.getElementById("addrequirements_id").addEventListener("click", () => {
    inputcontainer = document.getElementById('requirements_tags_id');
    inputValue = inputcontainer.value;
    inputField = document.getElementById("requirement_id");


    if (inputValue) {
        inputField.value += inputValue + ",,";

        const tagHolder = document.getElementById('addRequirementHolder');

        const newTag = document.createElement('p');
        newTag.textContent = inputValue;
        newTag.classList.add('addedREquirements');
        
        tagHolder.appendChild(newTag);
        }

    inputcontainer.value = "";
    

});



document.getElementById('CTN_id').addEventListener('change', (event) => {

    inputValue = event.target.value.replace(/^0+/, '');
    countryCode = document.getElementById('countryCode').value;

    sendNumber = document.getElementById('ContactNumber');
    sendNumber.value = countryCode + inputValue;

});

document.getElementById('ContactEmail_id').addEventListener('change', (event) => {

    inputValue = event.target.value;

    sendNumber = document.getElementById('ContactNumber');
    sendNumber.value = inputValue;

});




document.getElementById("ContactMethod").addEventListener("change", (event) => {
    if (event.target.value === "Email") {
        document.getElementById("CTN_id").value = "";
        document.getElementById("flag_ID").value = "";

        document.getElementById("ContactEmail_id").style.display = "block";
        document.getElementById("CTN_id").style.display = "none";
        document.getElementById("flag_ID").style.display = "none";
    } else {
        document.getElementById("ContactEmail_id").value = "";

        document.getElementById("ContactEmail_id").style.display = "none";
        document.getElementById("CTN_id").style.display = "block";
        document.getElementById("flag_ID").style.display = "block";
    }
})


document.getElementById("preview_id").addEventListener("click", () => {
    document.getElementById("previewContainer_id").style.display = "block";

    const select = document.getElementById("City");
    const tradesSelect = document.getElementById("Trade_Type");

    function previewing() {
        document.getElementById("neededTrades_ID").innerText = tradesSelect.options[tradesSelect.selectedIndex].text + " " + "needed"
        document.getElementById("Title_fix_ID").innerText = document.getElementById("Job_Title").value || "Not Specified";
        document.getElementById("detailVAlueBudget_ID").innerText = document.getElementById("Budget_Range").value || "Not Specified";
        document.getElementById("detailVAlueBLocation_ID").innerText = select.options[select.selectedIndex].text || "Not Specified";
        document.getElementById("detailVAlueCity_ID").innerText = document.getElementById("Budget_Type").value || "Not Specified";
        document.getElementById("detailVAlueJobType_ID").innerText = document.getElementById("Job_Type").value || "Not Specified";
        document.getElementById("detailVAlueUrgency_ID").innerText = document.getElementById("Ugency_level").value || "Not Specified";
        document.getElementById("detailVAlueMaterial_ID").innerText = document.getElementById("Materials_Provided").value || "\"Not Specified\"";
        document.getElementById("detailVAlueStarting_ID").innerText = document.getElementById("Start_date").value || "Not Specified";
        document.getElementById("detailVAlueEnding_ID").innerText = document.getElementById("End_date").value || "Not Specified";
        document.getElementById("detailVAlueEnvironment_ID").innerText = document.getElementById("Work_Environment").value || "Not Specified";
        document.getElementById("detailVAlueDeadline_ID").innerText = document.getElementById("Expiry_Date").value || "Not Specified";

        document.getElementById("discriptionText_ID").innerText = document.getElementById("Job_Description").value || "Not Specified";
        
    }

    function previewingTags() {
        const value = document.getElementById("Required_Skills").value;
        const tags = value.split(",");
        
        tags.forEach(tag => {

            if (tag) {
                const tagHolder = document.getElementById('skillSet_ID');

                const newTag = document.createElement('p');
                newTag.textContent = tag;
                
                tagHolder.appendChild(newTag);
            }          
        });
    }

    document.getElementById("Id_imageUpplad").addEventListener("change", (event) => {
        const Images = event.target.files;
        const previewContainer = document.getElementById("items_id")
        previewContainer.innerHTML = "";


        Array.from(Images).forEach(image => {
            const reader = new FileReader();
            reader.onload = function(e) {
                const imgElement = document.createElement('img');
                imgElement.src = e.target.result;

                previewContainer.appendChild(imgElement);
            };
            reader.readAsDataURL(image)
        })
        
        
    })

    function previewingRequirement() {
        const Value = document.getElementById('requirement_id').value;
        const requirements = Value.split(",");

        requirements.forEach(requirement => {

            if (requirement) {
                
                const divHolder = document.getElementById('additionalRequirements_id');

                const newDiv = document.createElement('div');
                newDiv.classList.add('adds');
                newDiv.innerHTML = `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <g clip-path="url(#clip0_203_230)">
                            <path d="M23.34 9.481L19.84 3.481C18.947 1.951 17.292 1 15.521 1H8.452C6.681 1 5.025 1.951 4.133 3.481L0.632001 9.481C-0.272999 11.034 -0.272999 12.964 0.632001 14.519L4.133 20.519C5.026 22.049 6.68 22.999 8.451 22.999H15.52C17.291 22.999 18.946 22.049 19.839 20.519L23.339 14.518C24.244 12.964 24.244 11.034 23.339 9.48L23.34 9.481ZM21.611 13.512L18.112 19.512C17.576 20.43 16.583 21 15.52 21H8.451C7.389 21 6.395 20.43 5.86 19.512L2.36 13.513C1.816 12.58 1.816 11.421 2.36 10.489L5.86 4.489C6.395 3.571 7.388 3 8.451 3H15.52C16.582 3 17.576 3.57 18.111 4.489L21.611 10.489C22.155 11.422 22.155 12.58 21.611 13.512ZM17 12C17 12.552 16.553 13 16 13H13V16C13 16.553 12.553 17 12 17C11.447 17 11 16.553 11 16V13H8C7.447 13 7 12.552 7 12C7 11.448 7.447 11 8 11H11V8C11 7.448 11.447 7 12 7C12.553 7 13 7.448 13 8V11H16C16.553 11 17 11.448 17 12Z" fill="#24FF24"/>
                            </g>
                            <defs>
                            <clipPath id="clip0_203_230">
                            <rect width="24" height="24" fill="white"/>
                            </clipPath>
                            </defs>
                        </svg> <p>${requirement}</p>`
                
                divHolder.appendChild(newDiv);
            }          
        });

    }

    function previewContact () {

        const container = document.getElementById('callBTN_id')

        if (document.getElementById("CTN_id").value) {

            container.innerHTML = "";           
            container.innerHTML = `<svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
<path fill-rule="evenodd" clip-rule="evenodd" d="M17.005 2.90667C15.1333 1.03333 12.645 0.000833333 9.99417 0C4.53167 0 0.0858333 4.445 0.0833333 9.91C0.0825 11.6567 0.539167 13.3617 1.40667 14.865L0 20L5.25333 18.6217C6.70083 19.4117 8.33083 19.8275 9.98917 19.8283H9.99333C15.455 19.8283 19.9017 15.3825 19.9042 9.9175C19.9058 7.27 18.8758 4.77917 17.005 2.90667ZM9.99417 18.1542H9.99083C8.5125 18.1542 7.06333 17.7567 5.79833 17.0058L5.4975 16.8275L2.38 17.645L3.2125 14.605L3.01667 14.2933C2.19167 12.9817 1.75667 11.4658 1.7575 9.91C1.75917 5.36833 5.455 1.67333 9.99833 1.67333C12.1983 1.67333 14.2667 2.53167 15.8217 4.08833C17.3767 5.64583 18.2325 7.715 18.2317 9.91583C18.2292 14.4592 14.5342 18.1542 9.99417 18.1542ZM14.5125 11.985C14.265 11.8608 13.0475 11.2617 12.82 11.1792C12.5933 11.0967 12.4283 11.055 12.2625 11.3025C12.0967 11.55 11.6233 12.1083 11.4783 12.2742C11.3342 12.4392 11.1892 12.46 10.9417 12.3358C10.6942 12.2117 9.89583 11.9508 8.95 11.1067C8.21417 10.45 7.71667 9.63917 7.5725 9.39083C7.42833 9.1425 7.5575 9.00917 7.68083 8.88583C7.7925 8.775 7.92833 8.59667 8.0525 8.45167C8.1775 8.30833 8.21833 8.205 8.30167 8.03917C8.38417 7.87417 8.34333 7.72917 8.28083 7.605C8.21833 7.48167 7.72333 6.2625 7.5175 5.76667C7.31667 5.28333 7.1125 5.34917 6.96 5.34167C6.81583 5.33417 6.65083 5.33333 6.485 5.33333C6.32 5.33333 6.05167 5.395 5.825 5.64333C5.59833 5.89167 4.95833 6.49083 4.95833 7.70917C4.95833 8.92833 5.84583 10.1058 5.96917 10.2708C6.0925 10.4358 7.715 12.9375 10.1992 14.01C10.79 14.265 11.2517 14.4175 11.6108 14.5317C12.2042 14.72 12.7442 14.6933 13.1708 14.63C13.6467 14.5592 14.6358 14.0308 14.8425 13.4525C15.0492 12.8742 15.0492 12.3775 14.9867 12.275C14.925 12.1708 14.76 12.1092 14.5125 11.985Z" fill="white"/>
</svg><p>${document.getElementById('CTN_id').value}</p>`;

        } else if (document.getElementById("ContactEmail_id").value) {

            container.innerHTML = "";

            container.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" id="Outline" viewBox="0 0 24 24" width="20" height="20" fill="white"><path d="M19,1H5A5.006,5.006,0,0,0,0,6V18a5.006,5.006,0,0,0,5,5H19a5.006,5.006,0,0,0,5-5V6A5.006,5.006,0,0,0,19,1ZM5,3H19a3,3,0,0,1,2.78,1.887l-7.658,7.659a3.007,3.007,0,0,1-4.244,0L2.22,4.887A3,3,0,0,1,5,3ZM19,21H5a3,3,0,0,1-3-3V7.5L8.464,13.96a5.007,5.007,0,0,0,7.072,0L22,7.5V18A3,3,0,0,1,19,21Z"/></svg>
<p> ${document.getElementById('ContactEmail_id').value} </p>`;
        } else {
            container.innerHTML =`<p>Not Specified</p>`
        }
    };

    document.getElementById('callMethod_id').innerText = `Preferred Contact Method: ${document.getElementById("ContactMethod").value}`;

    previewingTags();
    previewing();
    previewingRequirement();
    previewContact();
})



document.getElementById("previewDone").addEventListener("click", () => {

    document.getElementById("Title_fix_ID").innerText = "";
        document.getElementById("detailVAlueBudget_ID").innerText = "";
        document.getElementById("detailVAlueBLocation_ID").innerText = "";
        document.getElementById("detailVAlueCity_ID").innerText = "";
        document.getElementById("detailVAlueJobType_ID").innerText = "";
        document.getElementById("detailVAlueUrgency_ID").innerText = "";
        document.getElementById("detailVAlueMaterial_ID").innerText = "";
        document.getElementById("detailVAlueStarting_ID").innerText = "";
        document.getElementById("detailVAlueEnding_ID").innerText = ""
        document.getElementById("detailVAlueEnvironment_ID").innerText = "";
        document.getElementById("detailVAlueDeadline_ID").innerText = "";
        document.getElementById("discriptionText_ID").innerText = "";

        document.getElementById('skillSet_ID').innerHTML = "";
        document.getElementById("items_id").innerHTML = "";
        /* document.getElementById('additionalRequirements_id').innerHTML = ""; */
        document.getElementById('callBTN_id').innerHTML = "";


    document.getElementById("previewContainer_id").style.display = "none";
});


