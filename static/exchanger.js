var instructions;
var response_sent = false;

// This is isn't declared as `async` because it already returns a promise

function get_response() {
  var response = played_card.toString();
  console.log("response: " + response)
  return response;
}

(function(){
    document.addEventListener("DOMContentLoaded", function(event) {
    document.querySelectorAll('img').forEach(function(img){
    	 img.onerror = function(){this.style.display='none';};
    })
});})

function loadPic(id){$(`#${id}`).attr("src", `/static/${id}.png?` + d.getTime());}

function update_stuff() {
    $.get('/static/instructions.txt', function(data) {
        $("#instructions").text(data);
    })

    d = new Date();
    ['card1','card2','card3','card4','card5','card6','card7','black_card'].forEach(loadPic);

    setTimeout(function(){
        console.log(1);
        var blank = $("img").attr("src").match(/blank.png/);

        // this causes the code to break, I haven't been able to figure out why
        if(blank){
            $("img").attr({hidden: true});
        }
        else {
            $("img").attr({hidden: false});
        }
    },300);
}


// Hopefully don't have to change anything below this line

new Promise(function(resolve, reject) {
    // do a thing, possibly async, then…
    update_stuff();
    resolve('it worked.');
}).then(function () {
    return fetch('/hello');
}).then(function (response) {
    return response.text();
}).then(function (text) {
    // Print the instructions as text
    console.log('GET instruction text:');
    console.log(text);
    //instructions = JSON.parse(text)['instructions'];
    update_stuff();
    return parseInt(JSON.parse(text)['time_lim']) * 1000;
}).then(function(time_lim) {
    played_card = -1;
    return time_lim;
}).then(function(time_lim) {
    /*
    setTimeout(function (time_lim) {
      card_played = parseInt(prompt('what card do you want to play?'));
    }, time_lim / 2)*/
    var i;
    for (i = 1000; i < time_lim; i += 1000) {
        setTimeout(function (i) {
            if (get_response() != "-1" && !response_sent) {
                response_sent = true;
                send_response();
            }
        }, i);
    }
    setTimeout(function (time_lim) {
        if (!response_sent) {
            response_sent = true;
            send_response();
        }
    }, time_lim);
})

function send_response() {
    fetch('/hello', {
        // Specify the method
        method: 'POST',
        body: JSON.stringify({
            "response": get_response()
        })
    }).then( function () {
      played_card = -1;
      window.location.reload();
    })
}
