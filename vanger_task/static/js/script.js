
$(document).ready(function(){
    // Инициализация Slick Slider Syncing [[23]]
    $('.slider-for').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.slider-nav'
    });
    
    $('.slider-nav').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        asNavFor: '.slider-for',
        dots: false,
        centerMode: true,
        focusOnSelect: true,
        responsive: [{
            breakpoint: 768,
            settings: { slidesToShow: 2 }
        }, {
            breakpoint: 480,
            settings: { slidesToShow: 1 }
        }]
    });
    
    // Lightbox функционал
    const $lightbox = $('#lightbox');
    const $lightboxImg = $('#lightbox-img');
    let currentImageIndex = 0;
    // const images = {% for item in images %}"{{ item.image.url }}"{% if not forloop.last %},{% endif %}{% endfor %};    что с этим делать?
    const images = {}
    
    // Открытие lightbox по клику на большое изображение
    $('.slider-main-image').on('click', function() {
        currentImageIndex = parseInt($(this).data('index'));
        showLightbox(currentImageIndex);
    });
    
    function showLightbox(index) {
        if (images.length === 0) return;
        $lightboxImg.attr('src', images[index]);
        $lightbox.addClass('active');
        $('body').css('overflow', 'hidden');
    }
    
    function closeLightbox() {
        $lightbox.removeClass('active');
        $('body').css('overflow', '');
    }
    
    // Навигация в lightbox
    $('.lightbox-close').on('click', closeLightbox);
    
    $('.lightbox-next').on('click', function(e) {
        e.stopPropagation();
        currentImageIndex = (currentImageIndex + 1) % images.length;
        showLightbox(currentImageIndex);
    });
    
    $('.lightbox-prev').on('click', function(e) {
        e.stopPropagation();
        currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
        showLightbox(currentImageIndex);
    });
    
    // Закрытие по клику вне изображения
    $lightbox.on('click', function(e) {
        if ($(e.target).is($lightbox)) closeLightbox();
    });
    
    // Управление клавиатурой
    $(document).on('keydown', function(e) {
        if (!$lightbox.hasClass('active')) return;
        if (e.key === 'Escape') closeLightbox();
        if (e.key === 'ArrowRight') {
            currentImageIndex = (currentImageIndex + 1) % images.length;
            showLightbox(currentImageIndex);
        }
        if (e.key === 'ArrowLeft') {
            currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
            showLightbox(currentImageIndex);
        }
    });
});
