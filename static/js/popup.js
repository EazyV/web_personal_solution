const form = document.getElementById('form_applicant');
const form2 = document.getElementById('form_customer');
const popup = document.getElementById('popup');
const closeButton = document.querySelector('.close-button');
const submitButton = document.getElementById('send');
const submitButton2 = document.getElementById('customer_send');


submitButton.addEventListener('click', function (event) {
    if (form.checkValidity()) {
        popup.style.display = 'block';
    } else {
        // Если поля не заполнены, выводим сообщение об ошибке
        alert('Пожалуйста, заполните все поля формы.');
    }
});

closeButton.addEventListener('click', function () {
    popup.style.display = 'none';
    form.reset();
    form2.reset();
});

window.addEventListener('click', function (event) {
    if (event.target == popup) {
        popup.style.display = 'none';
        form.reset();
        form2.reset();
    }
});

popup.addEventListener('click', function (event) {
    popup.style.display = 'none';
    form.reset();
    form2.reset();
});

submitButton2.addEventListener('click', function (event) {
    if (form2.checkValidity()) {
        popup.style.display = 'block';
    } else {
        // Если поля не заполнены, выводим сообщение об ошибке
        alert('Пожалуйста, заполните все поля формы.');
    }
});







document.querySelector('#applicant_phone').onkeydown = function (e) {
    inputphone(e, document.querySelector('#applicant_phone'))
}

//Функция маски формат +7 (
function inputphone(e, phone) {
    function stop(evt) {
        evt.preventDefault();
    }

    let key = e.key, v = phone.value;
    not = key.replace(/([0-9])/, 1)

    if (not == 1 || 'Backspace' === not) {
        if ('Backspace' != not) {
            if (v.length < 3 || v === '') {
                phone.value = '+7('
            }
            if (v.length === 6) {
                phone.value = v + ')'
            }
            if (v.length === 10) {
                phone.value = v + '-'
            }
            if (v.length === 13) {
                phone.value = v + '-'
            }
        }
    } else {
        stop(e)
    }
}

document.querySelector('#customer_phone').onkeydown = function (e) {
    inputphone(e, document.querySelector('#customer_phone'))
}

//Функция маски формат +7 (
function inputphone(e, phone) {
    function stop(evt) {
        evt.preventDefault();
    }

    let key = e.key, v = phone.value;
    not = key.replace(/([0-9])/, 1)

    if (not == 1 || 'Backspace' === not) {
        if ('Backspace' != not) {
            if (v.length < 3 || v === '') {
                phone.value = '+7('
            }
            if (v.length === 6) {
                phone.value = v + ')'
            }
            if (v.length === 10) {
                phone.value = v + '-'
            }
            if (v.length === 13) {
                phone.value = v + '-'
            }
        }
    } else {
        stop(e)
    }
}