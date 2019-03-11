import socket

dictionary = {}                                         # Dictionary that will hold the key-value pairs
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# HTTP return messages
HTTP = 'HTTP/1.1 '
OK = HTTP + '200 OK'
UNSUPPORTED = HTTP + '220 UNSUPPORTED'
BAD_REQUEST = HTTP + '400 BAD_REQUEST'
NOT_FOUND = HTTP + '404 NOT FOUND'
print("I am here")

# Implement the get function that returns the value for the specific key from the dictionary
def get(x):
    print("I am in get")
    if(x == dictionary.get(x)):
        print(OK)
    elif(x != dictionary):
        print(NOT_FOUND)
    


# Implement the put function that updates the value for the specific key in the dictionary
def put(x, y):
    dictionary[x] = y
    print(OK)


# Implement the delete function that will remove the key-value pair from the dictionary
def delete(x):
    dictionary.pop[x]
    print(OK)

# Implement the delete function that will remove all the key-value pairs from the dictionary
def clear():
    dictionary.clear()
    print(OK)


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
             # Create a socket object
    host = '127.0.0.1' # Get local machine name
    port = 2000                # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port

    s.listen(5)                 # Now wait for client connection.
    while True:
        c, addr = s.accept()     # Establish connection with client.
        print ('Got connection from', addr)
        while True:
            print("Why am I here")
            modifiedConnected = c.recv(1024)
            message = modifiedConnected.decode()
            print(message)
            split = message.split(' ')
            print(split)
            if(split[0].lower() == 'get'):
                if(len(split) > 2):
                    print(BAD_REQUEST)
                    break;
                get(split[1])
                continue;
            elif(split[0].lower() == 'put'):
                if(len(split) > 3):
                    print(BAD_REQUEST)
                    break;
                x = split[1]
                y = split[2]
                put(x, y)
                continue;
            elif(split[0].lower() == 'delete'):
                if(len(split) > 2):
                    print(BAD_REQUEST)
                    break;
                delete(split[1])
            elif(split[0].lower() == 'clear'):
                if(len(split) > 1):
                    print(BAD_REQUEST)
                    break;
                clear()
            elif(split[0].lower() == 'quit'):
                if(len(split) > 1):
                    print(BAD_REQUEST)
                    break;
                quit()
            else:
                print(UNSUPPORTED)
                continue;
        

if __name__ == '__main__':
    main()
