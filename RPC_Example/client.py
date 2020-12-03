from json import loads, dumps
from socket import socket, AF_INET, SOCK_STREAM
from struct import pack, unpack


class RPC_Client:
    def __init__(self):
        self.client = socket(AF_INET, SOCK_STREAM)

    def init_conn(self):
        self.client.connect(("127.0.0.1", 9595))

    def close_conn(self):
        self.client.close()


    def __getattr__(self, item):
        def worker(*args):
            self.init_conn()
            data = dumps({
                'method' : item,
                'argv'   : list(args)
            })

            data_len = pack("<I", len(data))

            self.client.send(data_len)
            self.client.send(data.encode())

            response_len = unpack("<I",self.client.recv(4))[0]

            if not response_len:
                print("Serwer nie zwrocil zadnej odpowiedzi")
                exit()

            response = self.client.recv(response_len)

            if len(response) != response_len:
                print("Nie udalo sie odebrac wszystkich danych")
                exit()

            print("[*] CLIENT: received response: ", response)
            self.close_conn()
        return worker


clRPC = RPC_Client()
clRPC.upper('abc')


