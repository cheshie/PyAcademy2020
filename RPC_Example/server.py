from json import loads, dumps
from socket import socket, AF_INET, SOCK_STREAM
from struct import unpack, pack
import rpc_methods

class Server:
    def __init__(self):
        self.server = socket(AF_INET, SOCK_STREAM)
        self.server.bind(("127.0.0.1", 9595))
        self.server.listen(5)
    #

    def set_up(self):
        while True:
            cl, addr = self.server.accept()
            # print("srv: ", cl.recv(4))
            # exit()
            data_len = unpack("<I", cl.recv(4))[0]

            if not data_len:
                print("Niepoprawna dlugosc")
                exit()

            data = cl.recv(data_len)

            if data_len != len(data):
                print("Nie udalo sie odebrac wszysktich danych")
                exit()

            data_dct = loads(data)

            # Sprawdzic czy dane sa poprawne, czy nie wykorzystuja potencjalnych bledow bezpieczenstwa
            method, argv = data_dct['method'], data_dct['argv']

            if method not in rpc_methods.rpc_method.registry.keys():
                print("Server nie obsluguje danej metody!")
                exit()

            # TODO: sprawdz czy wszystkie argumenty sie zgadzaja

            # Wykonaj metode na serwerze
            returned = rpc_methods.rpc_method.registry[method](*argv)

            # Zwrotka do klienta
            returned_json = dumps(returned)
            returned_json_len = len(returned_json)
            cl.send(pack('<I', returned_json_len))
            cl.send(returned_json.encode())

            cl.close()


sv = Server()

try:
    sv.set_up()
except KeyboardInterrupt:
    exit()