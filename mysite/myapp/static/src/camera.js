setInterval( function() {
    $.ajax({
        url: "camera/",
        type: "GET",
        success: function(data) {
            $('#camera').css("background-image", 'url("' + data + '")')
        },
        error: function(data) {
            alert('No frames received!')
        },
    });
}, 1000);

