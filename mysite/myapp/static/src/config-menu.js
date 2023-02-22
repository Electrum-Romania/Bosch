$('.menu-button').on('click', function(e) {
    e.preventDefault();
    var $el = $(this);
    $el.addClass("clicked").siblings().removeClass('clicked');
});

var frame = "";

$('.frame').on('click', function(e) {
    e.preventDefault();
    var $el = $(this);
    frame = this.id;
});

var main = ""

$('.horizontal.menu-button').on('click', function(e) {
    e.preventDefault();
    var $el = $(this);
    main = this.id;

    $('#' + this.id + "-icon").removeClass("visible").siblings().addClass('visible');
    $('#' + this.id + "-div").addClass("visible").siblings().removeClass('visible');
});

var second = "raw"

$('.vertical.menu-button.f').on('click', function(e) {
    e.preventDefault();
    var $el = $(this);
    second = this.id;

    $.ajax({
        url: "request_frame",
        type: "POST",
        data: {
            'analysis': frame + "=" + main + "_" + second,
        },
    })  

    console.log(frame + "=" + main + "_" + second);

});

$('.vertical.menu-button.m').on('click', function(e) {
    e.preventDefault();
    
    // $('#' + this.id + "-icon").removeClass("visible").siblings().addClass('visible');
    $('#' + this.id + "-div").addClass("visible").siblings().removeClass('visible');
});


