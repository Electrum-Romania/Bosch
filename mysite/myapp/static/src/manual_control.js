document.addEventListener('keydown', function(event) {
    if(event.keyCode == 87) { //w
        $("#forward").css({"box-shadow": "inset 0px 0px 1px 2px black"});
        $.ajax({
            url: "manual_control",
            type: "POST",
            data: {
                'pressed_key': 'w',
            },
        })
    }
    else if(event.keyCode == 65) { //a
        $("#left").css({"box-shadow": "inset 0px 0px 1px 2px black"});
        $.ajax({
            url: "manual_control",
            type: "POST",
            data: {
                'pressed_key': 'a',
            },
        })
    }
    else if(event.keyCode == 83) { //s
        $("#back").css({"box-shadow": "inset 0px 0px 1px 2px black"});
        $.ajax({
            url: "manual_control",
            type: "POST",
            data: {
                'pressed_key': 's',
            },
        })
    }
    else if(event.keyCode == 68) { //d
        $("#right").css({"box-shadow": "inset 0px 0px 1px 2px black"});
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
        $("#forward").css({"box-shadow": "unset"});
    }
    else if(event.keyCode == 65) { //a
        $("#left").css({"box-shadow": "unset"});
    }
    else if(event.keyCode == 83) { //s
        $("#back").css({"box-shadow": "unset"});
    }
    else if(event.keyCode == 68) { //d
        $("#right").css({"box-shadow": "unset"});
    }
});