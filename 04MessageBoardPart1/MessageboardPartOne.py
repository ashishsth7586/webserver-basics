#!/usr/bin/env python3
#
# Step one in building the message board server:
# An echo server for POST requests.
#
# Instructions:
# 
# This server should accept a POST request and return the value
# of "message" field in that request

# We need to add three things to the do_POST method to make it work:
#
# 1. Find and add the length of the request data.
# 2. Read the correct amount of request data.
# 3. Extract the "message" field from the request data.

#
# When we're done, we need to run the server and test it from the 
# browser using the message-board.html form. To check it, we can use
# test.py script.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

class MessageHandler(BaseHTTPRequestHandler):
	def do_POST(self):
		# For checking, how long the messsage was => Use the Content-length header.
		length = int(self.headers.get('Content-length', 0))
		# Read the correct amount of data from the request.
		data = self.rfile.read(length).decode()
		# Extract the "message" field from the request data.
		message = parse_qs(data)["message"][0]
		# send the message field back as the response.
		self.send_response(200)
		self.send_header("Content-type", "text/plain charset=utf-8")
		self.end_headers()
		self.wfile.write(message.encode())

if __name__ ==  "__main__":
	server_address = ('', 8000)
	httpd = HTTPServer(server_address, MessageHandler)
	httpd.serve_forever()