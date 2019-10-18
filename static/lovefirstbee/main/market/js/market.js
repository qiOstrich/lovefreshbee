$(function () {
    var alltype = $('#alltype');
    var commonsrt = $('#commonsort');

    alltype.click(function () {
        var common = $('#commonsort_second');
        var this_secone = $('#alltype_second');
        common.css({display: 'none'});
        commonsrt.find('span').find('span').removeClass('glyphicon glyphicon-chevron-up glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-down');

        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-down glyphicon glyphicon-chevron-up');
        this_secone.toggle();
    });

    commonsrt.click(function () {
        var all = $('#alltype_second');
        var this_second = $('#commonsort_second');
        all.css({display: 'none'});
        alltype.find('span').find('span').removeClass('glyphicon glyphicon-chevron-up glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-down');

        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-down glyphicon glyphicon-chevron-up');
        this_second.toggle();
    });


    $(".addShopping").click(function () {
        var goodsid = $(this).attr('goodsid');
        var $button = $(this);
        // alert(goodsid);
        $.get(
            '/cartApp/addGoods/',
            {'goodsid': goodsid,},
            function (data) {
                if (data['status'] == 200) {
                    $button.prev().html(data['goods_num'])
                } else {
                    window.open('/userApp/login/', target = '_self')
                }

            }
        )

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

                $button.next().html(msg['goods_num']);

                //msg是求情成功后得到的返回数据
            },
        });

    });

});