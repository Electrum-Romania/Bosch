$('input[type=range]').on('input', function() {
    
    $.ajax({
        url: "load",
        type: "POST",
        data: {
            'id': this.id,
            'value': this.value,
        },
        // success: function (data) {
        // },
        // error: function(data) {
        //     alert ("nok");
        // }
    })
    let slider = $('#' + this.id);
    $('#' + this.id + "-value").html(this.value);

    
});

$('.menu-button.load').on('click', function(e) {
    e.preventDefault();
    var $el = $(this);
    $el.removeClass('clicked');
    $('input[type=range]').each(function(slider) {
        var $slider = $(this);
        $.ajax({
            url: "load",
            type: "POST",
            data: {
                'id': slider.id,
                'value': slider.value,
            },
            success: function (data) {
                console.log(this.id + " " + this.value);
            },
            error: function(data) {
                console.log("ERROR" + this.id + " " + this.value);
            }
        })
    });
});