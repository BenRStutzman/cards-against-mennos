/*
This is the code the helps javascript communicate with Pythong
*/

var instructions;
var response_sent = false;

function get_response() { //return which card has been played
    var response = played_card.toString();
    console.log("response: " + response)
    return response;
}

function update_stuff() { //reload pictures and instructions
    $.get('/static/instructions.txt', function(data) {
        $("#instructions").text(data);
    })

    d = new Date();
    $("#card1").attr("src", "/static/card1.png?" + d.getTime());
    $("#card2").attr("src", "/static/card2.png?" + d.getTime());
    $("#card3").attr("src", "/static/card3.png?" + d.getTime());
    $("#card4").attr("src", "/static/card4.png?" + d.getTime());
    $("#card5").attr("src", "/static/card5.png?" + d.getTime());
    $("#card6").attr("src", "/static/card6.png?" + d.getTime());
    $("#card7").attr("src", "/static/card7.png?" + d.getTime());
    $("#black_card").attr("src", "/static/black_card.png?" + d.getTime());

}

// Hopefully don't have to change anything below this line

new Promise(function(resolve, reject) {
    update_stuff(); //reload everything
    resolve('it worked.');
}).then(function () {
    return fetch('/hello'); //wait for instructions from pythong
}).then(function (response) {
    return response.text();
}).then(function (text) {
    // Print the instructions as text
    console.log('GET instruction text:');
    console.log(text);
    update_stuff(); //reload pics and instructions
    return parseInt(JSON.parse(text)['time_lim']) * 1000;
    // return the time limit
}).then(function(time_lim) {
    played_card = -1; //reset played_card to -1 (meaning you haven't played any yet)
    return time_lim;
}).then(function(time_lim) {
    var i;
    for (i = 1000; i < time_lim; i += 1000) { //keep checking every second whether you've played a card
        setTimeout(function (i) {
            if (get_response() != "-1" && !response_sent) { //if you've played a card, send it and refresh
                response_sent = true;
                send_response();
            }
        }, i);
    }
    setTimeout(function (time_lim) { //final check; if you still haven't played a card, send '-1'
        if (!response_sent) {
            response_sent = true;
            send_response();
        }
    }, time_lim);
});

function send_response() {
    fetch('/hello', { //send the response as a JSON object
        method: 'POST',
        body: JSON.stringify({
            "response": get_response()
        })
    }).then( function () { //set the played_card back to -1 and refresh the page
      played_card = -1;
      window.location.reload();
    })
}
