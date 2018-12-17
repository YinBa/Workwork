import socket
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSocket.bind(("", 8080))

print("Start to Receive")

while True:
    try:
        recvData = udpSocket.recvfrom(1024)
        content, destInfo = recvData

        print("Content is %s" % content.decode("utf-8"))

    except:
        print("error")
        udpSocket.close()
        break
