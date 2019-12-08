from ClientServer.client_module import GameClient, timed_input
from browser_module import exchange, setup_server
from dealer import deal, deal_black
import sys, msvcrt, time

def time_lim_string(time_lim):
    return "You have " + str(time_lim) + " seconds."

host = input("Enter the host computer's IP address: ")
port = 1000

f = open('static/instructions.txt', 'w')
f.write('Hit enter in your terminal to join the game.')
f.close()

deal([])
deal_black("-1")
setup_server()

keep_playing = 'y'

while keep_playing.lower() == 'y':

    client = GameClient(host, int(port))
    event = ''
    deal([])
    deal_black("-1")
    open('static/instructions.txt', 'w').close() #clear instructions

    while event != 'server closed':
        while client.events.empty():
            continue
        event, details, time_lim, num_chars = client.events.get()
        print(event, end = '')
        if details:
            print(':', details)
        else:
            print()

        '''
        if event == "Welcome to Cards Against Mennonites!":
            exchange("Welcome to Cards Against Mennonites!")
        '''
        if event == "Here's your new hand." or event == "Here are the submissions":
            deal(details.split())
        elif event == "Here's the judge's card.":
            deal_black(details)
        elif event.startswith('The judge chose'):
            f = open('static/instructions.txt', 'w') #clear the instruction log
            f.write(event + "\n")
            f.close()
        elif (event == "These are the submissions. Waiting for the judge to decide..."):
            f = open('static/instructions.txt', 'w') #clear the instructions
            f.write(event)
            f.close()
            exchange('refresh', 0) #update the page
            time.sleep(10)
        elif (event == "You are the judge for this round. Waiting for responses..."):
            f = open('static/instructions.txt', 'a') #add to the instructions
            f.write(event)
            f.close()
            exchange('refresh', 0) #update the page
        elif event == 'Which card do you want to play?':
            f = open('static/instructions.txt', 'a') #add to the instructions
            f.write(event + "\n")
            f.write(time_lim_string(time_lim))
            f.close()
            #exchange('refresh', 0) #update the page
            response = str(int(exchange('refresh', time_lim)) - 1)
            if response == '-2':
                response = '0'
            print("sending:", response)
            client.send(response)
            f = open('static/instructions.txt', 'w') #clear responses
            f.write('Waiting for all the players to respond...')
            f.close()
            time.sleep(10)
        elif event == 'Which card wins?':
            f = open('static/instructions.txt', 'w') #clear the instruction log
            f.write(event + "\n")
            f.write(time_lim_string(time_lim))
            f.close()
            #exchange('refresh', 0) #update the page
            response = str(int(exchange('refresh', time_lim)) - 1)
            if response == '-2':
                response = '0'
            print("sending:", response)
            client.send(response)
        else:
            f = open('static/instructions.txt', 'a') #anything else, just add to the instructions
            f.write(event + "\n")
            f.close()
    exchange('refresh', 30) #give the remaining instructions
    client.stop()
    open('static/instructions.txt', 'w').close() #clear the instructions
    while msvcrt.kbhit(): #clears all previous keypresses
        msvcrt.getch()
    keep_playing = input("Play again (y/n)? ")
