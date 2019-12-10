'''
Once cam_server.py is running on someone's computer,
run this code to play the game.
It will prompt you to go to an address in your browser,
from which the game is displayed.
'''

from ClientServer.client_module import GameClient, timed_input
from browser_module import exchange, setup_server
from dealer import deal, deal_black
import sys, msvcrt, time

open('js_to_py.txt', 'w').close() #clear the communication text files
open('py_to_js.txt', 'w').close()

def time_lim_string(time_lim):
    return "You have " + str(time_lim) + " seconds."

def get_and_send_response(client):
    response = str(int(exchange('refresh', time_lim)) - 1) # get the browser's response
    if response == '-2':
        response = '0' #default to picking the first card if they didn't pick in time
    print("sending:", response)
    client.send(response)

host = input("Enter the host computer's IP address: ")
port = 1000

f = open('static/instructions.txt', 'w')
f.write('Play any blank card to join the game.') #initial instructions
f.close()


deal([]) #put a bunch of blank cards in your hand
deal_black("-1") #put a blank black card on screen
setup_server() #will prompt you to open your browser

exchange('refresh', 10000) #wait for you to join the game from your browser

keep_playing = 'y'

while keep_playing.lower() == 'y': #keep looping through this until they're done

    client = GameClient(host, int(port))

    #clear everything
    event = ''
    deal([])
    deal_black("-1")
    open('static/instructions.txt', 'w').close()

    while event != 'server closed':
        while client.events.empty(): #wait until the server has sent an event
            continue
        event, details, time_lim, num_chars = client.events.get()

        #print the event to terminal, mostly for debugging
        print(event, end = '')
        if details:
            print(':', details)
        else:
            print()

        if event == "Here's your new hand." or event == "Here are the submissions.":
            deal(details.split()) #deal the new cards into your hand
        elif event == "Here's the judge's card.":
            deal_black(details) #deal the new black card
        elif event.startswith('The judge chose'):
            f = open('static/instructions.txt', 'w') #clear the instruction log and add event
            f.write(event + "\n")
            f.close()
        elif (event == "These are the submissions. Waiting for the judge to decide..."):
            f = open('static/instructions.txt', 'w') #clear the instruction log and add event
            f.write(event)
            f.close()
            exchange('refresh', 0) #update the page
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

            get_and_send_response(client)

            f = open('static/instructions.txt', 'w') #clear responses
            f.write('Waiting for all the players to respond...')
            f.close()
            time.sleep(10)
        elif event == 'Which card wins?':
            f = open('static/instructions.txt', 'w') #clear the instruction log
            f.write(event + "\n")
            f.write(time_lim_string(time_lim))
            f.close()
            get_and_send_response(client)
        elif event == 'server closed':
            f = open('static/instructions.txt', 'a') #add to the instructions
            f.write('\n' + event)
            f.close()
        else:
            f = open('static/instructions.txt', 'a') #anything else, just add to the instructions
            f.write(event + "\n")
            f.close()
    #once the server closes...
    exchange('refresh', 10) #give the remaining instructions
    client.stop()
    open('static/instructions.txt', 'w').close() #clear the instructions
    while msvcrt.kbhit(): #clear all previous keypresses
        msvcrt.getch()
    keep_playing = input("Play again (y/n)? ")
