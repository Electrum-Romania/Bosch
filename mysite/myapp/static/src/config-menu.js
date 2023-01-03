$('.menu-button').on('click', function(e) {
    e.preventDefault();
    var $el = $(this);
    $el.addClass("clicked").siblings().removeClass('clicked');
    $('#' + this.id + "-icon").removeClass("visible").siblings().addClass('visible');
    $('#' + this.id + "-div").addClass("visible").siblings().removeClass('visible');
});