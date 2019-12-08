var instructions;
var response_sent = false;

// This is isn't declared as `async` because it already returns a promise

function get_response() {
  var response = played_card.toString();
  played_card = -1;
  return response;
}

function update_stuff() {
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
  // do a thing, possibly async, then…
  update_stuff();
  resolve('it worked.');
}).then(function () {
    return fetch('/hello');
  })
    .then(function (response) {
            return response.text();
    }).then(function (text) {
            // Print the instructions as text
            console.log('GET instruction text:');
            console.log(text);
            //instructions = JSON.parse(text)['instructions'];
            update_stuff();
            return parseInt(JSON.parse(text)['time_lim']) * 1000;
          }
          )
    .then(function(time_lim) {
      /*
      setTimeout(function (time_lim) {
        card_played = parseInt(prompt('what card do you want to play?'));
      }, time_lim / 2
    )
    */
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

    } )

function send_response() {
    fetch('/hello', {
        // Specify the method
        method: 'POST',
        body: JSON.stringify({
            "response": get_response()
        })
    }).then( function () {
      window.location.reload();
    })
    }
