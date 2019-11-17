from client_module import GameClient

try:
    host = input("Enter the host computer's IP address: ")
    port = input("Enter the port # being used on the host computer: ")
    client = GameClient(host, int(port))

    # This while loop is just to demonstrate how to send/receive events;
    # the loop itself isn't necessary.
    while True:
        inp = input("Press V to view events or S to send one to the server: ")
        if inp.lower() == 'v':
            # to receive an event from the server:
            if client.events.empty():
                print("No new events have been received.")
            while not client.events.empty():
                event, details = client.events.get()
                # Then do whatever you want with those; I'll just print them here
                print(event + ": " + details)
        elif inp.lower() == 's':
            # To send an event to the server, do this.
            # This will add an event to the
            # "events" queue of the server, which can decide what to do with them.
            event = input("Enter event type: ")
            details = input("Enter event details: ")
            client.send(event, details)

except:
    print("Something went wrong; exiting game")

client.stop()
