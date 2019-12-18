$(function () {
    $('#all_type').click(function () {
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-up glyphicon glyphicon-chevron-down')
        $('#all_type_container').toggle()


    });
    $('#all_type_container').click(function () {
        $(this).toggle()
        $('#all_type').find('span').find('span').toggleClass('glyphicon glyphicon-chevron-up glyphicon glyphicon-chevron-down')
    });

    $('#sort_rule').click(function () {
        $(this).find('span').find('span').toggleClass('glyphicon glyphicon-chevron-up glyphicon glyphicon-chevron-down')
        $('#sort_rule_container').toggle()
    });
    $('#sort_rule_container').click(function () {
        $(this).toggle()
        $('#sort_rule').find('span').find('span').toggleClass('glyphicon glyphicon-chevron-up glyphicon glyphicon-chevron-down')
    });

    $('.addShopping').click(function () {
        var $button = $(this)
        // 获取标签自带的属性值
        // var className = $button.prop('class')
        //可以获取标签自带的属性值，也可以获取自定义的属性值
        var goodsId = $button.attr('goodsId')
        $.get(
            '/cartApp/addToCart/',
            {'goodsId': goodsId},
            function (data) {
                if (data['status'] == 200){
                    $button.prev().html(data['goodsNum'])
                }else {
                    window.location.href = '/userApp/login/'
                }
            }
        )
    })

    $('.subShopping').click(function () {
        var $button = $(this)
        // 获取标签自带的属性值
        // var className = $button.prop('class')
        //可以获取标签自带的属性值，也可以获取自定义的属性值
        var goodsId = $button.attr('goodsId')
        $.get(
            '/cartApp/subToCart/',
            {'goodsId': goodsId},
            function (data) {
                if (data['status'] == 200){
                    $button.next().html(data['goodsNum'])
                }else {
                    if(data['status']==201){
                        console.log(data)
                    }else {
                        window.location.href = '/userApp/login/'
                    }
                }
            }
        )
    })
});


