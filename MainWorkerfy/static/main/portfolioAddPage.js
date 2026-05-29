document.getElementById("CancelBTNmain").addEventListener("click", () => {
    document.getElementById("CancelPopUp").style.display = "flex";
})

document.getElementById("ContinueEditing").addEventListener("click", () => {
    document.getElementById("CancelPopUp").style.display = "none";
})

// API submit call
const form = document.getElementById('PORTFOLIOFORM');
if (form) {
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const submitButton = document.querySelector('.save-btn');
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

        fetch(`/api/v1/portfolio-items/`, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            }
        })
        .then(response => {
            if (response.status === 201) {
                const createdConfirnmation = document.querySelector('.created');
                if (createdConfirnmation) {
                    createdConfirnmation.style.display = 'flex';
                }
                console.log('Profile updated successfully');
                return response.json();
            }
            console.log('Raw response:', response); // Debugging line
            console.log('Response status:', response.status); // Debugging line
            return "Failed";
        })
        .then(data => {
            if (data !== "Failed") {
                console.log('Success:', data);
                // Redirect or show success message
            } else {
                console.error('Failed to update profile');
            };
            
        })
        .catch(error => {
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

