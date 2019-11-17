Instructions for using the Client-Server system.

The idea is that the players (client) and game (server) communicate by sending
"events" back and forth... for example, to have players draw cards, the server
could send an event with a new random card to each player. To submit cards,
the clients could each send an event with their chosen card to the server. Each event
has two parts: "event" (e.g. "new card" or "submit card"), and "details" (i.e.
the name of the card). You can make these whatever you want though, there are no
set categories.

I. On the machine that will be the server:
  A. Place the PodSixNet folder, cam_server.py, and server_module.py in the same directory
  B. Navigate to that directory and run cam_server.py
  C. It will prompt you to enter your IP address and choose a port

II. On the machines that will be the players/clients:
  A. Place the PodSixNet folder, cam_client.py, and client_module.py in the same directory
  B. Navigate to that directory and run cam_client.py
  C. It will prompt you to enter the IP address and port # that the server is using

In both programs, what follows is a loop where you can send events back and
forth and view newly received events. Feel free to get rid of this loop and use
the functions inside to match the game logic.
