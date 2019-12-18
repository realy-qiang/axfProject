$(function(){
    initWhell()
    initMustBuy()
});

function initWhell() {
    var mySwiper = new Swiper('#topSwiper', {
        loop:true,
        autoplay:3000,
        autoplayDisableOnInteraction:false,

        // 如果需要分页器
        pagination: '.swiper-pagination',

        // // 如果需要前进后退按钮
        // nextButton: '.swiper-button-next',
        // prevButton: '.swiper-button-prev',
        //
        // // 如果需要滚动条
        // scrollbar: '.swiper-scrollbar',
    })
}

function initMustBuy() {
    var mySwiper1 = new Swiper('#swiperMenu',{
        slidesPerView:3
    })
}