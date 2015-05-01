import os, struct, socket

def main():
    # Take screenshot and load the data.
    os.system('screencapture image.png')
    with open('image.png', 'rb') as file:
        data = file.read()

    # Construct message with data size.
    size = struct.pack('!I', len(data))
    message = size + data

    # Open up a server socket.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 65000))
    server.listen(5)

    # Constantly serve incoming clients.
    while True:
        client, address = server.accept()
        print('Sending data to:', address)

        # Send the data and shutdown properly.
        client.sendall(message)
        
        # recmsg = client.recv(1024);
        # while recmsg != "SHUT DOWN":
        #      recmsg = client.recv(1024);

        # print "Received '"+str(recmsg)+"'. Will close connection now"
        # client.close()

        # SHUT DOWN not working with OS X
        #client.shutdown(socket.SHUT_RDWR)
        break;


if __name__ == '__main__':
    main()