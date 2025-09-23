function telNumberFormat(event) {
    const input = event.target.value.replace(/\D/g, '');
    const formattedNumber = input.replace(/(\d{3})(\d{3})(\d{4})/, '$1 $2 $3');
    event.target.value = formattedNumber;
    };

function changeImage(event) {
    /* alert('hello');
    const input = event.target.value;
    alert(typeof input);
    let holder = document.getElementById('imageHolder');
    alert(holder);
    holder.setAttribute('scr', input); */
    document.getElementById('ProfilePicture').addEventListener('change', function(event) {
    const [file] = event.target.files;
    if (file) {
        document.getElementById('imageHolder').src = URL.createObjectURL(file);
    }
});
}


document.getElementById('Phone').addEventListener('input', function(event) {telNumberFormat(event)});
document.getElementById('OtherPhone').addEventListener('input', function(event) {telNumberFormat(event)});

document.getElementById('PersonalInformation').onclick = function() {
    if (document.getElementById('FName').value && document.getElementById('LName').value && document.getElementById('Other').value && document.getElementById('id_date_of_birth').value && (document.getElementById('id_gender').value || document.getElementById('Female') )) {
        document.getElementById('bulb1').style.backgroundColor = "#0000ff";
        document.getElementById('bulb2').style.backgroundColor = "#0000ff";
        document.getElementById('bulb1').style.boxShadow = "0 0 8px 0 green";
        document.getElementById('bulb1').style.border = "none";

    } else{
        document.getElementById('bulb1').style.backgroundColor = "gray";
        document.getElementById('bulb1').style.border = "1px solid #6b0404ff";
    }
};

document.getElementById('ContactInformation').onclick = function() {
    if (document.getElementById('Phone').value || document.getElementById('OtherPhone').value) {
        document.getElementById('bulb3').style.backgroundColor = "#0000ff";
        document.getElementById('bulb2').style.backgroundColor = "#0000ff";
        document.getElementById('bulb2').style.boxShadow = "0 0 8px 0 green";
        document.getElementById('bulb2').style.border = "none";
    } else{
        document.getElementById('bulb2').style.backgroundColor = "gray";
        document.getElementById('bulb2').style.border = "1px solid #6b0404ff";
    }
};

document.getElementById('LocationInformation').onclick = function() {
    if (document.getElementById('id_base_location').value && document.getElementById('id_sub_location').value && document.getElementById('id_work_areas').value) {
        document.getElementById('bulb4').style.backgroundColor = "#0000ff";
        document.getElementById('bulb3').style.backgroundColor = "#0000ff";
        document.getElementById('bulb3').style.boxShadow = "0 0 8px 0 green";
        document.getElementById('bulb3').style.border = "none";
    } else{
        document.getElementById('bulb3').style.backgroundColor = "gray";
        document.getElementById('bulb3').style.border = "1px solid #6b0404ff";
    }
};

document.getElementById('TradesInformation').onclick = function() {
    if (document.getElementById('id_trade_category').value && document.getElementById('id_trade_specialties').value && document.getElementById('id_skills').value) {
        document.getElementById('bulb5').style.backgroundColor = "#0000ff";
        document.getElementById('bulb4').style.backgroundColor = "#0000ff";
        document.getElementById('bulb4').style.boxShadow = "0 0 8px 0 green";
        document.getElementById('bulb4').style.border = "none";
    } else{
        document.getElementById('bulb4').style.backgroundColor = "gray";
        document.getElementById('bulb4').style.border = "1px solid #6b0404ff";
    }
};

document.getElementById('TradesDone').onclick = function() {
    if (document.getElementById('id_trade_category').value && document.getElementById('id_trade_specialties').value && document.getElementById('id_skills').value) {
        document.getElementById('bulb5').style.backgroundColor = "#0000ff";
        document.getElementById('bulb5').style.boxShadow = "0 0 8px 0 green";
        document.getElementById('bulb5').style.border = "none";
    } else{
        document.getElementById('bulb5').style.backgroundColor = "gray";
        document.getElementById('bulb5').style.border = "1px solid #6b0404ff";
    }
};
function pop(event) {
    alert('hello');
}

document.getElementById('ProfilePicture').addEventListener('input', function(event) {changeImage(event)});
