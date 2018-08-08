#
# Created by Christophe Duchesne for Positive Degree
# 2018/08/06
#

import socket

port_number = 3196


def establish_connection(hostname, port_number):
    pass


# To test connection with a particular unit
def main():

    port_number = 3196
    s = socket.socket()
    test_client_address = "192.168.2.253"
    host = socket.gethostname()
    port = port_number

    s.connect((test_client_address, port))
    print(s.recv(1024))
    s.close()


if __name__ == "__main__":
    main()
