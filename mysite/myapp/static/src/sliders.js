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
    document.querySelectorAll('input[type=range]').forEach(function(slider) {
        // var $slider = $(this);
        $.ajax({
            url: "load",
            type: "POST",
            data: {
                'id': slider.id,
                'value': slider.value,
            },
            success: function (data) {
                console.log(slider.id + " " + slider.value);
            },
            error: function(data) {
                console.log("ERROR: " + slider.id + " " + slider.value);
            }
        })
    });
});