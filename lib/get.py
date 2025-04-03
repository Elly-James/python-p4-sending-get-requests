# Importing the 'requests' library, which is used to send HTTP requests, such as GET and POST.
# It helps interact with web services or APIs.
import requests

# Importing the 'json' library, which is used for working with JSON data (parsing, creating, and manipulating).
# It helps to convert between Python objects and JSON (JavaScript Object Notation) formatted data.
import json

# The URL where we are fetching JSON data from. It points to a sample JSON file on a web server.
url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/locations.json"

# Sending a GET request to the specified URL. The 'requests.get()' method is used to retrieve data from the server.
# The server's response is stored in the 'response' variable.
response = requests.get(url)

# The 'response.text' attribute contains the raw content of the server's response, which is a JSON string.
# We use 'json.loads()' to parse this string and convert it into a Python dictionary (or list, depending on the structure).
# 'json.loads()' stands for "load string", and it converts the JSON string into a Python object.
json_content = json.loads(response.text)

# The 'json.dumps()' method converts a Python object (in this case, the 'json_content' dictionary) back into a JSON string.
# The 'indent=4' argument specifies that the JSON string should be pretty-printed with an indentation level of 4 spaces.
# This makes the output easier to read. The result is printed out using the 'print()' function.
print(json.dumps(json_content, indent=4))
