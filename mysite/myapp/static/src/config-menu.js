$('.menu-button').on('click', function(e) {
    e.preventDefault();
    var $el = $(this);
    $el.addClass("clicked").siblings().removeClass('clicked');
    $('#' + this.id + "-icon").removeClass("visible").siblings().addClass('visible');
    $('#' + this.id + "-div").addClass("visible").siblings().removeClass('visible');
});

var main = ""

$('.horizontal.menu-button').on('click', function(e) {
    e.preventDefault();
    var $el = $(this);
    main = this.id;
});

var second = ""

$('.vertical.menu-button').on('click', function(e) {
    e.preventDefault();
    var $el = $(this);
    second = this.id;

    $.ajax({
        url: "request_frame",
        type: "POST",
        data: {
            'analysis': main + " " + second,
        },
    })  

});
