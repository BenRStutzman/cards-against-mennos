function get_response(instructions) {

  return prompt(instructions);

}

// Hopefully don't have to change anything below this line
exchange()
function exchange() {
    fetch('/hello')
    .then(function (response) {
            return response.text();
    }).then(function (text) {
            // Print the instructions as text
            console.log('GET instruction text:');
            console.log(text);
            return text;
    }).then(function (text) {
        return fetch('/hello', {
            // Specify the method
            method: 'POST',
            body: JSON.stringify({
                "response": get_response(JSON.parse(text)['instructions'])
            })
        })
    }).then(function (response) {
        return response.text();
    }).then(function (text) {
        console.log('POST response: ');
        // Should be 'OK' if everything was successful
        console.log(text);
        return window.location.reload()
    })
  }
