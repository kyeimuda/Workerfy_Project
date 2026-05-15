document.getElementById('BOOKBTN').addEventListener('click', () => {
    document.getElementById('BOOKBTN').style.visibility = 'hidden';
    document.querySelector('.bookingProcess').style.display = 'flex';
});

document.getElementById('CANCELBTN').addEventListener('click', () => {
    document.querySelector('.bookingProcess').style.display = 'none';
    document.getElementById('BOOKBTN').style.visibility = 'visible';
});

