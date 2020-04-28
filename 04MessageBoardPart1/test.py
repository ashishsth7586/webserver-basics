 
#!/usr/bin/env python3
#
# Test script for the Messageboard Part One server.
#
# The server should be listening on port 8000 and answer a POST request
# with an echo of the "message" field.

import requests, random, socket

def test_connect():
	""" Try connecting to the server """

	print("Testing connecting to the server")
	try:
		with socket.socket() as s:
			s.connect(("localhost", 8000))
		print("Connection attempt succeeded.")
		return None
	except socket.error:
		return "Server didn't answer on localhost port 8000. Is it running?"

def test_POST():
	"""The server should accept a POST and return the 'nessage' field"""
	print("Testing POST request.")
	msg = random.choice(["Hellow!", "Hi!! you", "Greetings!!!"])
	uri = "http://localhost:8000/"

	try:
		r = requests.post(uri, data={'message': msg})
	except requests.RequestException as e:
		return (f"Couldn't communicate with the server. ({e}), If it's running, take a look at its output. ")

	if r.status_code == 501:
		return ("The server returned status code 501 Not Implemented. \
			This means it doesn't know how to handle a POST request. \
			Is the correct server code running?")

	elif r.status_code != 200:
		return(f"The server returned status code {r.status_code} instead of a 200 OK")

	elif r.text != msg:
		return(f"The server sent a 200 OK response, but the content differed. \
			I expected {msg}, but it sent {r.text}")
	else:
		print("POST request succeeded")
		return None

if __name__ == '__main__':
    tests = [test_connect, test_POST]
    for test in tests:
        problem = test()
        if problem is not None:
            print(problem)
            break
    if not problem:
        print("All tests succeeded!")