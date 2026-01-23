$('#auth-button').click(
    function() {
        let email = $('#email').val();
        let password = $('#password').val();
        let csrf = $('[name=csrfmiddlewaretoken]').val();

        if(!email) {
            alert('Введите адрес почты');
        }

        if(!password) {
            alert('Введите пароль');
        }

        $.ajax({
            url: '/auth/',
            type: 'POST', // отправляем POST-запрос на сервер
            dataType: 'json',
            data: {
                'email' : email,
                'password' : password,
                'csrfmiddlewaretoken': csrf
            },
            success: function(data) {
                window.location.href = '/';
            },
            error: function(data) {
                console.log('error auth');
            }
        });
    }
);