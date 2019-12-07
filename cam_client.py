from ClientServer.client_module import GameClient, timed_input
from browser_module import exchange, setup_server
from dealer import deal
import sys, msvcrt



host = input("Enter the host computer's IP address: ")
port = input("Enter the port # being used on the host computer: ")

deal([], 'white')
setup_server()

keep_playing = 'y'

while keep_playing.lower() == 'y':

    client = GameClient(host, int(port))
    event = ''
    deal([], 'white')

    while event != 'server closed':
        while client.events.empty():
            continue
        event, details, time_lim, num_chars = client.events.get()
        print(event, end = '')
        if details:
            print(':', details)
        else:
            print()
        if time_lim > 0 and num_chars > 0:
            response = timed_input(
                    str.format("Give a %d-character response within %d seconds: "
                    % (num_chars, time_lim)), time_lim, num_chars)
            client.send(response)

        if event == 'Your hand':
            deal(details.split(), 'white')
        else:
            exchange(event)

    client.stop()
    while msvcrt.kbhit(): #clears all previous keypresses
        msvcrt.getch()
    keep_playing = input("Play again (y/n)? ")
