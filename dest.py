import socket, struct

def main(host):
    # Connect to server and get image size.
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, 65000))
    except Exception as e:
        print str(e)

    packed = recvall(client, struct.calcsize('!I'))

    # Decode the size and get the image data.
    size = struct.unpack('!I', packed)[0]
    print("Size of image: "+str(size))
    print('Receiving data from:', host)
    data = recvall(client, size)

    # Shutdown the socket and create the image file.
    print "Shutting down connection"
    #client.shutdown(socket.SHUT_RDWR)
    client.send("SHUT DOWN")
    client.close()

    with open('image_out.png', 'wb') as file:
        file.write(data)

def recvall(sock, size):
    message = bytearray()

    print "Start receiving image-data"

    # count packages
    i = 0

    # Loop until all expected data is received.
    while len(message) < size:
        buffer = sock.recv(size - len(message))
        
        print "received package #"+str(i)
        i = i+1

        if not buffer:
            # End of stream was found when unexpected.
            raise EOFError('Could not receive all expected data!')
        message.extend(buffer)

    #print "Finished receiving: "+str(message)
    return bytes(message)

if __name__ == '__main__':
    main('localhost')