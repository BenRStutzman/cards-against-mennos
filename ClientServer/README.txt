cards-against-mennos

A Software Engineering Project by Austin Engle, Dan Hackman, Isaac Andreas, and Ben Stutzman

Dan and Isaac: Game Logic
Ben: Client-server stuff
Austin: Javascript/display

Instructions for using the Client-Server system.

I. Add game logic to the cam_server.py file. It has the basic template ready,
   but it needs the meat of the game. The 3 server functions available to you are:

   A. server.send_event(event, details = "", player_ID = -1, time_lim = -1, num_chars = -1)
    - Sends an event to the player with player_ID, and gives them time_lim seconds
        to respond with num_chars characters.
    - if details is not specified, this will just be like sending a message
    - If player_ID is not specified, this will send to all players
    - If time_lim or num_chars aren't specified, this will send an event
        that doesn't ask for a response

   B. server.get_responses(num_needed = -1)
    - Waits until it has received at least num_needed responses, then
        returns all responses as a list of tuples (player_ID, response)
    - This will automatically clear responses when it finishes
    - If num_needed is not specified, this will wait until
        it has a response from all players

   C. server.clear_responses()
    - Clears the queue of all past responses (shouldn't really be needed)

II. On the machine that will be the server:
  A. Place the PodSixNet folder, cam_server.py, and server_module.py in the same directory
  B. Navigate to that directory and run cam_server.py

III. On the machines that will be the players/clients:
  A. Place the PodSixNet folder, cam_client.py, and client_module.py in the same directory
  B. Navigate to that directory and run cam_client.py
  C. It will prompt you to enter the IP address and port # that the server is using
  D. From then on it's controlled by the events the server sends
