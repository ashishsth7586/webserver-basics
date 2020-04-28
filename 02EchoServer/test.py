import requests, random

words = ["Ashish", "Shrestha", "Python", "Go", "Tango", "Uniform", "Delta",
		"Computer", "Alien", "Github", "Whiskey", "Lullaby"]

query = "".join(random.choice(words) for _ in range(3))
uri = "http://localhost:8000/" + query
print(f"Sending query for: {uri}")

try:
	r = requests.get(uri)
	output = r.text.strip()
	if r.status_code != 200:
		print(f"The server returned status code {r.status_code} instead of a 200 OK")
	elif output == query:
		print("Wow! Looks good!")
	else:
		print("The server sent a 200 OK response, but it wasn't an echo.")
		print(f"I expected '{query}', but the server said '{output}'")
		if output == 'Hello, Client this is HTTP! response on your request.':
			print("That looks like the hello server talking.")
except requests.ConnectionError:
	print("Couldn't connect to the server. Is it running on port 8000?")
except requests.RequestException as e:
	print(f"Couldn't communicate with the server ({e})")
	print(f"If it's running, take a look at the server's output.")
