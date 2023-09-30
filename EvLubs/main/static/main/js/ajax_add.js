$(document).ready(function ($) {
    $('#ad').click(function () {
        console.log('ok')
        $.ajax({
            type: 'POST',
            data: $(this).serialize(), // получаяем данные формы
            url: this.action,
            // headers: {'X-CSRFToken': getCookie('csrftoken')},
            success: function (response) {
                console.log('ok -', response)
            },
            error: function (response) {
                console.log('err - ', response)
            }
        });
        return false;
    });
})