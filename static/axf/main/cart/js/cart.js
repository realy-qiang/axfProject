$(function () {
    $('.addShopping').click(function () {
        var $button = $(this);
        // 获取标签自带的属性值
        // var className = $button.prop('class')
        //可以获取标签自带的属性值，也可以获取自定义的属性值
        var goodsId = $button.attr('goodsId');
        $.get(
            '/cartApp/addToCart/',
            {'goodsId': goodsId},
            function (data) {
                if (data['status'] === 200) {
                    $button.prev().html(data['goodsNum']);
                    $('.total').html(data['total']);
                } else {
                    window.location.href = '/userApp/login/'
                }
            }
        )
    });

    $('.subShopping').click(function () {
        var $button = $(this);
        // 获取标签自带的属性值
        // var className = $button.prop('class')
        //可以获取标签自带的属性值，也可以获取自定义的属性值
        var goodsId = $button.attr('goodsId');
        $.get(
            '/cartApp/subToCart/',
            {'goodsId': goodsId},
            function (data) {
                if (data['status'] === 200) {
                    $button.next().html(data['goodsNum']);
                    $('.total').html(data['total']);
                    if (data['goodsNum'] === 0) {
                        $button.parent().parent().remove();
                        if(!data['is_have_goods']){
                            $('.checkAll').children().html('')
                        }
                    }
                } else {
                    if (data['status'] === 202) {
                        window.location.href = '/userApp/login'
                    }
                }
            }
        )
    });
    $('.check').click(function () {
        var $button = $(this);
        $button.children().toggle();
        var goodsId = $button.attr('goodsId');

        $.ajax({
            type: 'get',
            url: '/cartApp/changeCheck/?goodsId=' + goodsId,
            success: function (data) {
                var display = $button.children().css('display');
                $('.total').html(data['total']);

                if (!data['is_true']) {
                    $('.checkAll').children().css('display', 'none')
                } else {
                    $('.checkAll').children().css('display', 'block')
                }
            }
        })
    });

    $('.checkAll').click(function () {
        var $button = $(this);
        var dispaly = $button.children().css('display');

        if (dispaly === 'none') {
            $button.children().toggle();
            $('.check').children().css('display', 'block');
            $.ajax({
                type: 'get',
                url: '/cartApp/changeAllCheck/?display='+dispaly,
                success: function (data) {
                    $('.total').html(data['total'])
                }
            })
        } else {
            $button.children().toggle();
            $('.check').children().css('display', 'none');
            $.ajax({
                type: 'get',
                url: '/cartApp/changeAllCheck/?display='+dispaly,
                success: function (data) {
                    $('.total').html(data['total'])
                }
            })
        }

    })

    $('.order_detail').click(function () {
        var select_list = [];
        var unselect_list = [];

        $('.check').each(function () {
            if($(this).children().css('display') == 'block'){
                var goodId = $(this).attr('goodsId')
                select_list.push(goodId)
            }else {
                unselect_list.push(goodId)
            }
        });

        if(select_list.length == 0){
            return;
        }else{
            // window.location.href = '/orderApp/order/'
            $.ajax({
                url:'/orderApp/order_detail/',
                type:'GET',
                dataType:'json',
                success:function (data) {
                    if(data['status']==200){
                        window.location.href = '/orderApp/order/?order_id='+data['order_id']
                    }
                }
            })
        }
    })

});