document.querySelector('.bookBTN').addEventListener('click', () => {
    document.getElementById('BOOKBTN').style.visibility = 'hidden';
    document.querySelector('.bookingProcess').style.display = 'flex';
});

document.getElementById('CANCELBTN').addEventListener('click', () => {
    document.querySelector('.bookingProcess').style.display = 'none';
    document.getElementById('BOOKBTN').style.visibility = 'visible';
});

const observedetailsGroup = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            const bulbs = document.querySelectorAll('.bulbs div');
            bulbs.forEach(bulb => bulb.classList.remove('activeBulb'));

            const headers = document.querySelectorAll('.headings p');
            headers.forEach(header => header.classList.remove('activeHeader'));
            
            const detailsGroupID = entry.target.id;
            if (detailsGroupID === 'basicInformation') {
                const bulb = document.querySelector('.basicInformationBulb');
                const header = document.querySelector('.basicInformationHeader');
                header.classList.add('activeHeader');
                header.scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center'});
                if (bulb) {
                    console.log(bulb);
                    bulb.classList.add('activeBulb');
                }
            } else if (detailsGroupID === 'JobPortFoilio') {
                const bulb = document.querySelector('.jobPortfolioBulb');
                const header = document.querySelector('.jobPortfolioHeader');
                header.classList.add('activeHeader');
                header.scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center'});
                if (bulb) {
                    console.log(bulb);
                    bulb.classList.add('activeBulb');
                }
            } else if (detailsGroupID === 'moreDetails') {
                const bulb = document.querySelector('.moreDetailsBulb');
                const header = document.querySelector('.moreDetailsHeader');
                header.classList.add('activeHeader');
                header.scrollIntoView({ behavior: 'smooth', block: 'center', inline: 'center'});
                if (bulb) {
                    console.log(bulb);
                    bulb.classList.add('activeBulb');
                }
            }
        }
    })
}, {
    threshold: 0.8   // 60% of the section must be visible
});

const detailsGroups = document.querySelectorAll('.detailsGroup');

detailsGroups.forEach(detailsGroup => observedetailsGroup.observe(detailsGroup));
