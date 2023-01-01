$('.menu-button').on('click', function(e) {
    e.preventDefault();
    var $el = $(this);
    $el.addClass("clicked").siblings().removeClass('clicked');
});