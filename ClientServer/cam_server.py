from server_module import GameServer

try:
    host = input("Enter this computer's IP address: ")
    port = input("Enter the port # you'd like to use (1000 is fine): ")
    server = GameServer(localaddr = (host, int(port)))

    # This while loop is just to demonstrate how to send/receive events;
    # the loop itself isn't necessary.
    while True:

        inp  = input("Press V to view events, S to send an event, or A to send"
                        " an event to all players")
        if inp.lower() == 'v':
            # to deal with all the events that have been sent
            # by the players, do this:
            if server.events.empty():
                print("No new events have been received.")
            while not server.events.empty():
                player, event, details = server.events.get()
                # Then do whatever you want with this information.
                # I'm just printing it as an example
                print(str(player.ID) + ": " + event + ": " + details)
        elif inp.lower() in 'sa':
            player_ID = int(input("Enter player ID: "))
            event = input("Enter event type: ")
            details = input("Enter event details: ")
            time_lim = int(input("Enter time limit in seconds: "))
            if inp.lower() == 's':
                # to send an event to a specific player, do this:
                server.send_to_player(player_ID, event, details, time_lim)
            elif inp.lower() == 'a':
                # to send an event to all the players, do this:
                server.send_to_all(event, details, time_lim)

except KeyboardInterrupt:
    print("Something went wrong; exiting game")

server.stop()
