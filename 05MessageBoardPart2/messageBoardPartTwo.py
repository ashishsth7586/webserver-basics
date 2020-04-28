#!/usr/bin/env python3
#
# Step two in building the messageboard server:
# A server that handles both GET and POST requests.
#

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

form = '''<!DOCTYPE html>
<html>
<head>
	<title>Message Board</title>
</head>
<body>
	<form method="POST" action="http://localhost:8000/">
		<textarea name="message"></textarea>
		<br>
		<button type="submit">Post it!</button>
	</form>

</body>
</html>'''

class MessageHandler(BaseHTTPRequestHandler):
	def do_POST(self):
		#  How long was the message?
		# Avoid using header['content-length']
		# If the request body is empty 
		# this code crashes. Hence we use dict method
		length = int(self.headers.get('Content-length', 0))
		
		# Read the correct amount of data from the request
		data = self.rfile.read(length).decode()
		
		# Extract the message field from the request data
		message = parse_qs(data)["message"][0]
		print(parse_qs(data))
		print(parse_qs(data)["message"])

		# Send the message field back as the response
		self.send_response(200)
		self.send_header('Content-type', 'text/plain; charset=utf-8')
		self.end_headers()
		self.wfile.write(message.encode())

	def do_GET(self):

		# First, send a 200 OK response.
		self.send_response(200)

		# Then send headers
		self.send_header('Content-type', 'text/html; charset=utf-8')
		self.end_headers()

		# Then encode and send the form

		self.wfile.write(form.encode())

if __name__ == "__main__":
	server_address = ('', 8000)
	httpd = HTTPServer(server_address, MessageHandler)
	httpd.serve_forever()