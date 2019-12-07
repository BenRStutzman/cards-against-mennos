For this to work, you need to have flask installed. To do this, just type
"pip install flask" in command prompt. (If you don't have pip, which should come
with python, you'll need to get pip or find another way to get flask).

The idea is that each player can run the RUN_ME.py file on their own computer,
which will run a server on their browser that displays stuff with javascript.

Right now, javascript takes instructions from python, prompts the user in the browser,
and then sends back their response. But this can hopefully be made more complicated,
like sending back the ID number of whichever card they clicked on or something.

***Austin:***
To change the javascript stuff, change what's inside the get_response function
at the top of templates/index.html.

The key to the python stuff is the exchange() function in RUN_ME, which takes
a string of instructions as input and sends that to the javascript, then waits for
a response and returns that to python. We'll hopefully be able to integrate that
into the cam_client.py program.
