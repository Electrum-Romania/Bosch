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
});

$('input[type=range]').on('input', function() {
    
    $.ajax({
        url: "load",
        type: "POST",
        data: {
            'analysis': main + " " + second,
        },
    })  
});