$(function () {
    $('.addShopping').click(function () {
        var $button = $(this);
        var goodsid = $button.attr('goodsid');
        $.ajax({
            url: "/cartApp/addGoods/", //路径，链接
            type: "get",//请求方式 get post putpatch delete
            data: {
                "goodsid": goodsid,
            },//发送的数据，可以是text，json
            dataType: "json",//返回数据格式，text，json，xml
            success: function (msg) {

                $button.prev().html(msg['goods_num']);
                $("#total_price").html(msg['total_price']);
                //msg是求情成功后得到的返回数据
            },
        });

    });

    $('.subShopping').click(function () {
        var $button = $(this);
        var goodsid = $button.attr('goodsid');
        $.ajax({
            url: "/cartApp/subGoods/", //路径，链接
            type: "get",//请求方式 get post putpatch delete
            data: {
                "goodsid": goodsid,
            },//发送的数据，可以是text，json
            dataType: "json",//返回数据格式，text，json，xml
            success: function (msg) {

                if (msg['goods_num']) {
                    $button.next().html(msg['goods_num']);
                } else {
                    $button.parent().parent(".menuList").remove();

                }
                $("#total_price").html(msg['total_price']);

                //msg是求情成功后得到的返回数据
            },
        });

    });

    $('.confirm').click(function () {
        var $selected = $(this);
        var all_select = $('#all_toggle').attr('all_select');


        $.ajax({
            url: "/cartApp/changeStatus/", //路径，链接
            type: "get",//请求方式 get post putpatch delete
            data: {
                "goodsid": $selected.attr('goods_id'),
                'all_select': all_select,
            },//发送的数据，可以是text，json
            dataType: "json",//返回数据格式，text，json，xml
            success: function (msg) {

                if (msg['c_status']) {
                    $selected.find("span").find("span").html('√');

                } else {
                    $selected.find("span").find("span").html('');

                }

                if (msg['all_select']) {
                    $('#all_toggle').find("span").find("span").html("√");
                    $('#all_toggle').attr('all_select', '1');
                } else {
                    $('#all_toggle').find("span").find("span").html("");
                    $('#all_toggle').attr('all_select', '0');
                }
                $("#total_price").html(msg['total_price']);

            },
        });


    });

    $('#all_toggle').click(function () {
        var $all_confirm = $('.confirm');
        $.ajax({
            url: "/cartApp/changeAll/", //路径，链接
            type: "GET",//请求方式 get post putpatch delete
            data: {'all_status': $(this).attr('all_select'),},//发送的数据，可以是text，json
            dataType: "json",//返回数据格式，text，json，xml
            success: function (msg) {


                if (msg['all_select']) {

                    $all_confirm.find("span").find("span").html('√');
                    $('#all_toggle').attr('all_select', '1');
                } else {
                    $all_confirm.find("span").find("span").html('');
                    $('#all_toggle').attr('all_select', '0');
                }


                $("#total_price").html(msg['total_price']);

            },
        });
    })

});







