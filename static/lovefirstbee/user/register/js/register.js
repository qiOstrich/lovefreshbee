$(function () {
    var nameFlag = 0;
    var emailFlag = 0;
    var passwordFlag = 0;
    var fileFlag = 0;

    //判断按钮是否可以点击
    function buttonCheck() {
        if (nameFlag && emailFlag && passwordFlag && fileFlag) {
            $('#register_submit').removeAttr('disabled');
        } else {
            $('#register_submit').attr('disabled', 'disabled');
        }
    }

    //判断用户名是否能用
    $('#register_userid').blur(function () {

        var name = $(this).val();

        var recompile = /^[a-zA-Z]{5,32}$/;
        var register_name = recompile.test(name);


        if (register_name) {
            $.getJSON('/userApp/checkName/',
                {'name': name},
                function (msg) {

                    if (msg['status'] == 200) {
                        $('#namespan').html(msg['msg']).css({'color': 'green'});
                        nameFlag = 1;
                    } else {
                        $('#namespan').html(msg['msg']).css({'color': 'red'});
                        nameFlag = 0;
                    }
                }
            );
        } else {
            $('#namespan').html('×用户名格式错误').css({'color': 'red'});
            nameFlag = 0;
        }
        buttonCheck();

    });

    //判断邮箱格式是否正确
    $('#register_email').blur(function () {
        var email = $(this).val();
        var recompile = /@{1}\w+/;
        var register_email = recompile.test(email);
        if (register_email) {
            $('#emailspan').html('√').css({'color': 'green',});
            emailFlag = 1;
        } else {
            $('#emailspan').html('×请正确输入邮箱格式').css({'color': 'red',});
            emailFlag = 0;
        }
        buttonCheck();

    });

    //判断密码是否一直
    $('#register_reuserpwd').blur(function () {

        var pwd = $('#register_userpwd').val();
        var repwd = $(this).val();

        if (pwd) {
            if (pwd == repwd) {
                passwordFlag = 1;
                $('#pwdspan').html('√').css({'color': 'green',});

            } else {
                passwordFlag = 0;
                $('#pwdspan').html('×密码不一致').css({'color': 'red',});

            }
        } else {
            passwordFlag = 0;
            $('#pwdspan').html('×密码还是要的').css({'color': 'red',});
        }
        buttonCheck();
    });

    //测试文件是否上传
    $('#register_headerimg').blur(function () {
        var img = $('#register_headerimg').val();
        if (img) {
            fileFlag = 1;
        } else {
            fileFlag = 0;
        }

        buttonCheck();
    })

});

function password_md5() {
    var get_password = document.getElementById('register_userpwd').value;

    var get_repassword = document.getElementById('register_reuserpwd').value;
    var password = md5(get_password);

    document.getElementById('register_reuserpwd').value = password;
    document.getElementById('register_userpwd').value = password;

    return true
}