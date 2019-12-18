function changeCode() {
    var img = document.getElementById('changeImage');
    img.src = '/userApp/get_code/?'+Math.random()
}

function parse() {
    var password = document.getElementById('loginPassword1').value;
    var name = document.getElementById('loginName').value;
    var code = document.getElementById('loginCode').value;

    if(name.trim() == '' || password.trim() == ''){
        document.getElementById('isNull').innerHTML = '用户名或密码不能为空'
        return false
    }else {
        if(code.trim() == ''){
            document.getElementById('isCodeNull').innerHTML = '验证码不能为空';
            return false
        }else{
            password = md5(password);
            document.getElementById('loginPassword1').value = password;
            return true
        }

    }

}