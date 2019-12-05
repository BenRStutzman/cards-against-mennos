
import os
import re
from http.server import BaseHTTPRequestHandler

from routes.main import routes

from response.templateHandler import TemplateHandler
from response.badRequestHandler import BadRequestHandler
from response.staticHandler import StaticHandler


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
                regex = re.compile("word\d")
                if(regex.match(submtted)):
                    print("True")
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

    # def do_POST(self):
    #     print('Hello World!')
    #     print(self)

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
        response = self.handle_http(opts['handler'])
        self.wfile.write(response)
