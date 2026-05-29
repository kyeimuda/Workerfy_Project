function formatDate() {
    const date = document.querySelector('.datepostedAndID .dateposed p').textContent 
    if (date) {
        const dateToday = new Date(date);
        const today = new Date();
        const timeDiff = (today - dateToday);
        const days = Math.floor(timeDiff / (1000 * 60 * 60 * 24));

        if (days === 0) {
            const date = document.querySelector('.datepostedAndID .dateposed p').textContent = 'Posted today';
        } else {
            const date = document.querySelector('.datepostedAndID .dateposed p').textContent = `Posted ${days} days ago`;
        }

    }
}

function age() {
    const userDate = document.getElementById('Age');
    if (userDate) {
        const today = new Date();
        const birthDate = new Date(userDate.textContent);
        let age = today.getFullYear() - birthDate.getFullYear();
        const monthDiff = today.getMonth() - birthDate.getMonth();

        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
            age--;
        }

        userDate.textContent = `${age} yrs`;
    }       
}

formatDate()
age()

