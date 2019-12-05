
import os
import re
from http.server import BaseHTTPRequestHandler

from routes.main import routes

from response.templateHandler import TemplateHandler
from response.badRequestHandler import BadRequestHandler
from response.staticHandler import StaticHandler

# how to search several things -- tokenize? Possibly put this stuff into a convenience method
# basic structure of the url: root/#room/#user/#command/#options where # indicates a variable
# the next goal is to find a way to put in cookies/login info to track users
regex = []
regex.append(re.compile("/(card)(\d)")) #to play a card
regex.append(re.compile("/(draw)(\d)")) #to draw \d cards not implemented in js yet
i = 0

class Server(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return

    def do_GET(self):
        split_path = os.path.splitext(self.path)
        request_extension = split_path[1]
        submitted = split_path[0]


        if request_extension is "" or request_extension is ".html":
            if self.path in routes:
                handler = TemplateHandler()
                handler.find(routes[self.path])
            else:
                for pattern in regex:
                    match=pattern.match(submitted)
                    if(match):
                        handler = [match[1],match[2]]
                        break
                    else:
                        handler = BadRequestHandler()
        elif request_extension is ".py":
            handler = BadRequestHandler()
        else:
            handler = StaticHandler()
            handler.find(self.path)

        self.respond({
            'handler': handler
        })


    def handle_http(self, handler):
        status_code = handler.getStatus()

        self.send_response(status_code)

        if status_code is 200:
            content = handler.getContents()
            self.send_header('Content-type', handler.getContentType())
        else:
            content = "404 Not Found"

        self.end_headers()

        if isinstance( content, (bytes, bytearray) ):
            return content

        return bytes(content, 'UTF-8')

    def respond(self, opts):
        try:
            if(opts['handler'][0] == "card"):
                global i
                i+=1
            # need to send info to the server, which can be done from here?

            # this also currently runs 10 times... not sure why problably something about the unreliablility of the internet and needing to make sure the signal goes through
                print("Hello World!",i)
        except:
            response = self.handle_http(opts['handler'])
            self.wfile.write(response)
