$('input[type=range]').on('input', function() {
    $.ajax({
        url: "load/",
        type: "POST",
        data: {
            'id': this.id,
            'value': this.value,
        },
        // success: function (data) {
        //     alert (data);
        // },
        // error: function(data) {
        //     alert ("nok");
        // }
    
    })
    let slider = $('#' + this.id);
    $('#' + this.id + "-value").html(this.value);
})