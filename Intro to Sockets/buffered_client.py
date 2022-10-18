from socket import *
from struct import pack, unpack
# TODO: add any import statements required

class BufferedTCPClient:

    def __init__(self, server_host='localhost', server_port=36001, buffer_size=1024):
        self.buffer_size = buffer_size

        # TODO: Create a socket and establish a TCP connection with server 
        self.tcp_Client = socket(AF_INET, SOCK_STREAM)
        self.tcp_Client.connect((server_host, server_port))


    # This method is called by the autograder. You must implement it, and you cannot change the method signature. It should accept a message
    # from the user, which is packed according to the format specified for this assignment and then sent into the socket.
    # TODO: * Send a message to the server containing the message passed in to the function. 
    #           * Remember to pack it using the format defined in the instructions. 
    def send_message(self, message):
        print("Client: Attempting to send a message...")
        msg = message.encode()
        msg_length = len(message)
        packed_msg = pack("!I" + str(msg_length) + "s", msg_length, msg)
        self.tcp_Client.send(packed_msg)
        
        return
        


    # This method is called by the autograder. You must implement it, and you cannot change the method signature. It should wait to receive a 
    # message from the socket, which is then returned to the user. It should return two values: the message received and whether or not it was received 
    # successfully. In the event that it was not received successfully, return an empty string for the message.
    # TODO: * Return the *string* sent back by the server. This should be the same string you sent, except that first 10 characters will have been removed
    #           * Be sure to set the bufsize parameter to self.buffer_size when calling the socket's receive function
    #           * Remember that we're sending packed messages back and forth, for the format defined in the assignment instructions. You'll have to unpack
    #             the message and return just the string. Don't return the raw response from the server.
    #       * Handle any errors associated with the server disconnecting
    def receive_message(self):
        FIXED_HEADER_LENGTH = 4
        print("Client: Attempting to receive a message...")
        try:
            response = self.tcp_Client.recv(FIXED_HEADER_LENGTH)
        except ConnectionResetError as e:
            print("Client: Server shutdown")
            return "", False

        if(response):
            print("Client: Message received")
            payload_buffer = b""
            length = unpack('!I', response)[0] 
            while len(payload_buffer) < length:
                buffer_size = min(self.buffer_size, length - len(payload_buffer))
                data = self.tcp_Client.recv(buffer_size)
                payload_buffer += data 
            message = payload_buffer.decode()
            return message, True

        else:
            print("Client: Server forced disconnect")
            return "", False
            

        


    # This method is called by the autograder. You must implement it, and you cannot change the method signature. It should close your socket.
    # TODO: Close your socket
    def shutdown(self):
        print("Client: Attempting to shut down...")
        self.tcp_Client.close()
        print("Client: Socket closed..")
        return
        

        
if __name__ == "__main__":
    l = BufferedTCPClient(server_host="localhost", server_port=36001)

    l.send_message("Four score and seven years ago")
    response = l.receive_message()
    if(response[0] == "" or response[1] == False):
        l.shutdown()
        exit(0)
    print(response[0])

    for x in range(3):
        print("Client>>>")
        msg = input()
        l.send_message(msg)
        response = l.receive_message()
        if(response[0] == "" or response[1] == False):
            l.shutdown()
            exit(0)
        print(response[0])
    l.shutdown()
