setInterval( function() {
    $.ajax({
        url: "camera/",
        type: "GET",
        success: function(data) {
            let time = performance.now();
            $('#camera').css("background-image", 'url("' + data + '#' + time + '")');
            console.log('url("' + data + '#' + time + '")')
        },
        error: function(data) {
            // alert('No frames received!');
        },
    });
}, 1000);

