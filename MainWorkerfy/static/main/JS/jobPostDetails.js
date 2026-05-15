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

formatDate()

