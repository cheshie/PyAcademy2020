from collections import deque, namedtuple
from threading import Thread
from time import sleep

ramka_t = namedtuple('ramka_t', ['addr', 'data'])

class User():
    def __init__(self):
        pass
    def polacz(self, srv_addr, request):
        srv_addr.add(ramka_t(self, request))

    def receive(self, msg):
        print(f"[{self}]: Server returned: ", msg)
    def __str__(self):
        return "user1"


class Server():
    def __init__(self):
        def server_lp():
            while True:
                ramka = None
                try:
                    ramka = self.data.pop()
                except IndexError:
                    pass

                if ramka != None:
                    print(f"[{self}]: New request: ", ramka)
                    self.answer(ramka)
                else:
                    print(f"[{self}]: Nothing was requested")
                sleep(1) # wait 1 sec

        self.data = deque()
        self.main_loop = Thread(target=server_lp)
        self.main_loop.start()

    def add(self, request):
        self.data.append(request)

    def __str__(self):
        return "serv"

    # def show_queue(self):
    #     print("Currently in server's queue:")
    #     for x in self.data:
    #         print(x)

    def answer(self, ramka):
        ramka.addr.receive(ramka.data.upper())




if __name__ == "__main__":
    usr1 = User()
    srv  = Server()

    usr1.polacz(srv, 'abcd')

