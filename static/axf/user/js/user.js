$(function () {
    $('#exampleInputName').blur(function () {
        var name = $(this).val();

        var reg = /^[a-z]{3,6}$/;

        var is_true = reg.test(name);
        if (is_true) {
            // $('#nameInfo').html('✓用户名格式正确').css({'color':'green','font-size':10})
            // jquery请求方法 .getJSON .get .POST .AJAX
            // .getJSON请求格式 $.getJSON(url, 请求参数, 返回值)
            $.getJSON('/userApp/checkname/',
                {'name': name},
                function (data) {
                    if (data['status'] == 200) {
                        $('#nameInfo').html(data['msg']).css({'color': 'green', 'font-size': 10})
                    } else {
                        $('#nameInfo').html(data['msg']).css({'color': 'red', 'font-size': 10})
                    }
                })
        } else {
            $('#nameInfo').html('ㄨ用户名格式错误').css({'color': 'red', 'font-size': 10})
        }
    });

    $('#exampleInputPasswordConfirm').blur(function () {
        var password = $('#exampleInputPassword1').val();
        var passwordConfirm = $(this).val();
        if (password == passwordConfirm) {

        } else {
            $('#passwordConfirm').html('两次密码不一致，请重新输入').css({'color': 'red', 'font-size': 10})
        }

    });
});

function parse1() {
    var password = document.getElementById('exampleInputPassword1').value;
    var email = document.getElementById('exampleInputEmail').value;
    var fifle = document.getElementById('exampleInputFile').value;

    if (email.trim() == '') {
        document.getElementById('emailInfo').innerHTML = '邮箱不能为空';
        return false
    }

    if (password.trim() == '') {
        document.getElementById('passwordInfo').innerHTML = '密码不能为空';
        return false
    }

    password = md5(password);
    document.getElementById('exampleInputPassword1').value = password;
}