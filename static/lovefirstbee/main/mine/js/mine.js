$(function () {
    $("#to_login").click(function () {
        if ($(this).html() == '未登录') {
            window.location.href = '/userApp/login/';
            // window.open('/userApp/login/',target='_self');
        } else {

        }
    });

    $("#regis").click(function () {
        window.location.href = '/userApp/register/';
    });
});