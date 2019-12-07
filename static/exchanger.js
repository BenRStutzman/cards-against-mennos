var instructions;

// This is isn't declared as `async` because it already returns a promise

function get_response() {
  return played_card.toString();
}

// Hopefully don't have to change anything below this line
fetch('/hello')
    .then(function (response) {
            return response.text();
    }).then(function (text) {
            // Print the instructions as text
            console.log('GET instruction text:');
            console.log(text);
            instructions = JSON.parse(text)['instructions'];
            $("#instructions").text(instructions);
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
      setTimeout(function (time_lim) {
        send_response()
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
