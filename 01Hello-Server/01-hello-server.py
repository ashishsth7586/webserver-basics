"""
The `hello server` is an HTTP server that 
responds to a GET request by sending back a 
friendly greeting. Run this program in terminal
and access the server at http://localhost:8000 in a
web browser
"""

from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		"""
		In response, server needs to send: 1. a status code, 2. some headers
		3. response body.
		"""
		# First, send a 200 OK response.
		self.send_response(200) 

		# then send headers
		self.send_header('Content-type', 'text-plain; charset=utf-8') # key value pair
		self.end_headers()

		# Now, write the response body
		self.wfile.write("Hello, Client this is HTTP! response on your request. \n".encode())

if __name__ == '__main__':
	server_address = ('', 8000) # server on all address, port 8000
	httpd = HTTPServer(server_address, HelloHandler)
	httpd.serve_forever()
