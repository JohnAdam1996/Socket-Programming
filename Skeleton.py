import socket

dictionary = {}                                         # Dictionary that will hold the key-value pairs


# HTTP return messages
HTTP = 'HTTP/1.1 '
OK = HTTP + '200 OK'
UNSUPPORTED = HTTP + '220 UNSUPPORTED'
BAD_REQUEST = HTTP + '400 BAD_REQUEST'
NOT_FOUND = HTTP + '404 NOT FOUND'

s = socket.socket()
port = 2000
s.bind(('0.0.0.0', port))




# Implement the get function that returns the value for the specific key from the dictionary
def get():
    return


# Implement the put function that updates the value for the specific key in the dictionary
def put():
    return


# Implement the delete function that will remove the key-value pair from the dictionary
def delete():
    return


# Implement the delete function that will remove all the key-value pairs from the dictionary
def clear():
    return


# Implement the quit function that will end the connection with the client
def quit():
    return


# Implement the main function where we create, bind and listen to a socket. When a client is connection receive the
# message, decode the command and call the corresponding function. Server should send an answer to the client's request.
# When client closes the connection(quit) server should also close the connection. Bind your server to IP '0.0.0.0' so that
# it will listen to local connection requests.
def main():
	# You can use this operations dictionary to get the corresponding function: For example $func = operations['get'](params) is equal to $get(params) 
    operations = {'get': get, 'put': put, 'delete': delete, 'clear': clear, 'quit': quit}
    


if __name__ == '__main__':
    main()
