"""
Improvements:

1- Handle exceptions: Add error handling to manage potential issues, 
   such as connection errors.

2- Use context management: Use a context manager to ensure the socket 
   is properly closed.

3- HTTP/1.1: Use HTTP/1.1 instead of HTTP/1.0, which is more common and 
   allows for persistent connections.

4- Set Host header: Include the Host header in the HTTP request, which 
   is required for HTTP/1.1.

5- Simplify the request string: Format the request string more clearly.
"""


import socket

# Function to fetch the content of a URL


def fetch_url(url, host, port=80):
    request = f"GET {url} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"

    try:
        # Use context management to ensure the socket is closed
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as my_sock:
            my_sock.connect((host, port))
            my_sock.sendall(request.encode())

            response = b""
            while True:
                data = my_sock.recv(512)
                if not data:
                    break
                response += data

        # Split header and body
        header, body = response.split(b"\r\n\r\n", 1)

        # Decode and print the header & body
        print(header.decode())
        print('-----')
        print(body.decode())

    except socket.error as e:
        print(f"Socket error: {e}")


# Fetch the content of romeo.txt from data.pr4e.org
fetch_url("/romeo.txt", "data.pr4e.org")
fetch_url("/page1.htm", "www.dr-chuck.com")

"""
Key Improvements:
------------------
1. Function for URL Fetching:
- Encapsulated the logic in a function fetch_url to make it reusable.

2. Request String:
- Constructed the request string with HTTP/1.1 and included the Host header.

3. Context Manager:
- Used a with statement to ensure the socket is properly closed.

4. Error Handling:
- Added a try-except block to handle potential socket errors.

5. Efficient Response Handling:
- Accumulated the response data in a single response variable.
- Split the response into headers and body to discard the HTTP headers and only print the body.


Conclusion:

This improved code is more robust, adheres to modern HTTP practices, 
and ensures resources are properly managed.
"""


print('--------------------------------------------------------------')
