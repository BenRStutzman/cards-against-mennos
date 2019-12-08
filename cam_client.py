from ClientServer.client_module import GameClient, timed_input
from browser_module import exchange, setup_server
from dealer import deal, deal_black
import sys, msvcrt

def time_lim_string(time_lim):
    return "You have " + str(time_lim) + " seconds."

host = input("Enter the host computer's IP address: ")
port = 1000

deal([])
deal_black("-1")
setup_server()

keep_playing = 'y'

while keep_playing.lower() == 'y':

    client = GameClient(host, int(port))
    event = ''
    deal([])
    deal_black("-1")

    while event != 'server closed':
        while client.events.empty():
            continue
        event, details, time_lim, num_chars = client.events.get()
        print(event, end = '')
        if details:
            print(':', details)
        else:
            print()

        if event == "Here's your new hand." or event == "Here are the choices.":
            deal(details.split())
            exchange(event, 3)
        elif event == "Here's the judge's card.":
            deal_black(details)
            exchange(event, 3)
        elif event == 'Which card do you want to play?' or event == 'Which card wins?':
            client.send(int(exchange(event + " " + time_lim_string(time_lim), time_lim)) - 1)
        else:
            exchange(event, 3)

    client.stop()
    while msvcrt.kbhit(): #clears all previous keypresses
        msvcrt.getch()
    keep_playing = input("Play again (y/n)? ")
