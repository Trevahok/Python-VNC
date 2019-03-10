import socket
import tkinter as tk
from tkinter import Canvas
from PIL import ImageTk, Image
import time
from data import SocketData
import pickle
from threading import Thread

class Receiver:

    def __init__(self, open_sockets=10):
        self.data_string = ""
        self.length = 0
        self.open_sockets = open_sockets
        self.data = []

    def start(self):
        for i in range(self.open_sockets):
            t = Thread(target=self.receive, args=['127.0.0.1', 7000+i, i])
            t.start()

    def receive(self, host='127.0.0.1', port=6969, part_index=0):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as receiver:
            
            receiver.connect((host, port))

            buffer_size = int(receiver.recv(10).decode())
            print(buffer_size)
            
            byte_data = receiver.recv(buffer_size)
            self.data.insert(part_index, byte_data)
            #print(len(self.data))
            if len(self.data) == self.open_sockets:
                pickle.loads(b"".join(self.data)).image.show()

if __name__ == "__main__":
    r = Receiver().start()

    #time.sleep(2)
    #print(r.data)
    #r.receive() 

