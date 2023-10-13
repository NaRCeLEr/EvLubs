

function searc(a) {
    let value = a.value.trim().toLowerCase();
    let elasticItems = document.querySelectorAll('.elastic li');
    if (value != '') {
        elasticItems.forEach(function(el) {
            if (el.innerText.toLowerCase().search(value) == -1) {
                el.classList.add('hidden');
            }else {
                el.classList.remove('hidden');
            }
        });
    }
}

