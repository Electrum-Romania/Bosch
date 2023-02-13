document.addEventListener('keydown', function(event) {
    if(event.keyCode == 87) { //w
        $("#forward").css({"box-shadow": "inset 5em 1em gold"});
        $.ajax({
            url: "manual_control",
            type: "POST",
            data: {
                'pressed_key': 'w',
            },
        })
    }
    else if(event.keyCode == 65) { //a
        $.ajax({
            url: "manual_control",
            type: "POST",
            data: {
                'pressed_key': 'a',
            },
        })
    }
    else if(event.keyCode == 83) { //s
        $.ajax({
            url: "manual_control",
            type: "POST",
            data: {
                'pressed_key': 's',
            },
        })
    }
    else if(event.keyCode == 68) { //d
        $.ajax({
            url: "manual_control",
            type: "POST",
            data: {
                'pressed_key': 'd',
            },
        })
    }
});

document.addEventListener("keyup", (event) => {
    if(event.keyCode == 87) { //w

    }
    else if(event.keyCode == 65) { //a

    }
    else if(event.keyCode == 83) { //s

    }
    else if(event.keyCode == 68) { //d

    }
});