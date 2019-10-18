$(function () {
    var nameFlag = 0;
    var pwdFlag = 0;
    var codeFlag = 0;

    var code = $('#login_code');

    //用户名是否为空
    $('#login_userid').blur(function () {
        var name = $(this).val();
        if (name) {
            nameFlag = 1;
        } else {
            $("#useridspan").html('×用户名不能为空').css({'color': 'red',});
            nameFlag = 0;
        }
        buttoncanclick();


    });

    //密码是否为空
    $("#login_userpwd").blur(function () {
        var password = $(this).val();
        if (password) {
            pwdFlag = 1;
        } else {
            $("#userpwdspan").html('×密码不能为空').css({'color': 'red',});
            pwdFlag = 0;
        }
        buttoncanclick();
    });

    //验证码是否为空
    code.blur(function () {
        var checkcode = $(this).val();
        if (checkcode) {
            codeFlag = 1;
        } else {
            codeFlag = 0;
            $('#codespan').css({display: 'block'})
        }
        buttoncanclick()
    });

    code.focus(function () {
        var codeImg = $("#codeImg");
        codeImg.css({display: 'block'});
        $('#codespan').css({display: 'none'});

    });

    //点击图片进行切换
    $('#codeImg').click(function () {
        $(this).attr('src', '/userApp/get_code/?' + Math.random());
    });

    function buttoncanclick() {
        if (nameFlag && pwdFlag && codeFlag) {
            $("#login_submit").removeAttr('disabled');
        } else {
            $("#login_submit").attr('disabled', 'disabled');
        }
    }


});

function md5_password() {
    var password = document.getElementById('login_userpwd').value;
    password = md5(password);
    document.getElementById('login_userpwd').value = password;

    return true

}
