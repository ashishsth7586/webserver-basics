
#!/usr/bin/env python3
#
# The *echo server* is an HTTP server that responds to a GET request by
# sending the query path back to the client.  For instance, if the URI 
# "http://localhost:8000/Balloon" is requested, the echo server will respond
# with the text "Balloon" in the HTTP response body.

from http.server import HTTPServer, BaseHTTPRequestHandler

class EchoHandler(BaseHTTPRequestHandler):
	def do_GET(self):

		# First, send a 200 OK response.
		self.send_response(200)

		# Second, send the headers.
		self.send_header('Content-type', 'text/plain charset=utf-8')
		self.end_headers()
		
		# Third, send the response body
		message = self.path[1:] # for /balloon it returns balloon
		message_bytes_object = message.encode()
		self.wfile.write(message_bytes_object)

if __name__ == "__main__":
	server_address = ('', 8000)
	httpd = HTTPServer(server_address, EchoHandler)
	httpd.serve_forever()