$(function () {
    wheel();
    nav();
});

function wheel() {
    var mySwiper1 = new Swiper('#topSwiper', {
        loop: true,
        autoplay: 1000,
        pagination: '.swiper-pagination',
        autoplayDisableOnInteraction: false,


    });
};


function nav() {
    var mySwiper2 = new Swiper('#swiperMenu', {
        slidesPerView: 3,
        // paginationClickable: true,
        // spaceBetween: 2,
        // loop: false,
    });
};
