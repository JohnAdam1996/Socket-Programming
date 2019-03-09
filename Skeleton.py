import socket

dictionary = {}                                         # Dictionary that will hold the key-value pairs


# HTTP return messages
HTTP = 'HTTP/1.1 '
OK = HTTP + '200 OK'
UNSUPPORTED = HTTP + '220 UNSUPPORTED'
BAD_REQUEST = HTTP + '400 BAD_REQUEST'
NOT_FOUND = HTTP + '404 NOT FOUND'
print("I am here")

# Implement the get function that returns the value for the specific key from the dictionary
def get(x):
    if(x == dictonary[x]):
        return print(OK)
    elif(x != dictonary[x]):
        return print(NOT_FOUND)
    


# Implement the put function that updates the value for the specific key in the dictionary
def put(x):
    dictionary = [x]
    return


# Implement the delete function that will remove the key-value pair from the dictionary
def delete(x):
    if(x == dictonary[x]):
        dictonary.pop[x]
        return print(OK,"\nRemoved ", x)
    elif(x != dictonary[x]):
        return print(NOT_FOUND)

# Implement the delete function that will remove all the key-value pairs from the dictionary
def clear():
    dictionary.clear()
    return print(OK,"\nRemoved ", x)


# Implement the quit function that will end the connection with the client
def quit():
    print("Client has closed connection")
    s.close();


# Implement the main function where we create, bind and listen to a socket. When a client is connection receive the
# message, decode the command and call the corresponding function. Server should send an answer to the client's request.
# When client closes the connection(quit) server should also close the connection. Bind your server to IP '0.0.0.0' so that
# it will listen to local connection requests.
def main():
	# You can use this operations dictionary to get the corresponding function: For example $func = operations['get'](params) is equal to $get(params) 
    operations = {'get': get, 'put': put, 'delete': delete, 'clear': clear, 'quit': quit}
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
    host = '127.0.0.1' # Get local machine name
    port = 12345                # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port

    s.listen(5)                 # Now wait for client connection.
    while True:
        c, addr = s.accept()     # Establish connection with client.
        print ('Got connection from', addr)
        while True:
            print(operations[get])
            modifiedConnected = c.recv(1024)
            message = modifiedConnected.decode()
            print(message)
            if(message == operations['get']):
                get()
            elif(message == operations['put']):
                put()
            elif(message == operations['delete']):
                delete()
            elif(message == operations['clear']):
                clear()
            elif(message == operations['quit']):
                quit()
            else:
                print(BAD_REQUEST)

if __name__ == '__main__':
      main()
