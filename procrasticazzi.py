# Copyright 2011 Giovanni Totaro
# https://github.com/vannitotaro

from SimpleHTTPServer import SimpleHTTPRequestHandler
import SocketServer

class ReqRedirect(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = '/'
        SimpleHTTPRequestHandler.do_GET(self)
        
SocketServer.TCPServer(('localhost', 80), ReqRedirect).serve_forever()

