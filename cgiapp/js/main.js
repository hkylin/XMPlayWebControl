function updateSongTitle(currentTitle){
    var titleSpan = $("#song_title");
    $.ajax({
        type: "GET",
        url: "cgi-bin/get_title.py",
    }).done(function(msg) {
        jQuery.trim(msg);
        code = msg.slice(0,1);
        msg = msg.slice(1);
        if (titleSpan.text() != msg){
            titleSpan.text(msg);
            resetTimer();
        }
        if (code === "0"){
            stopTimer();
        }
    });
}

function changeSong(button){
    $.ajax({
        type: "GET",
        url: "cgi-bin/control.py",
        data: {action: button.data("action")}
    }).done(function(msg) {
        msg = jQuery.trim(msg);
        if (msg === "ok"){
            setTimeout(updateSongTitle, 500);
        }
    });

    switch (button.data("action")){
        case "play_pause":
            if (timer.getStatus()){
                timer.stop();
            }else{
                timer.start();
            }
            break;

        case "stop":
            stopTimer();
            break;

        default:
            break;
    }
}

function changeVolume(button){
    $.ajax({
        type: "GET",
        url: "cgi-bin/control.py",
        data: {action: button.data("action")}
    });

    switch (button.data("action")){
        case "vol_on_off":
            break;

        default:
            $("#button_vol_on_off").removeClass("active");
            break;
    }
}

function resetTimer(){
    timer.reset(0);
    timer.mode(1);
    timer.start();
}

function stopTimer(){
    timer.stop();
    timer.reset(0)
}

$(document).ready(function(){
    timer = new _timer();
    updateSongTitle();
    setInterval(updateSongTitle, 2000);

    $('#control_buttons').delegate('button', 'click', function() {
        changeSong($(this));
    });

    $('#volume_buttons').delegate('button', 'click', function() {
        changeVolume($(this));
    });
});