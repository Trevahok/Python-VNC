import socket
from PIL import Image
import time
from data import SocketData
import pickle

def recvall(receiver, buffer_size=65536):
    data_buffer = b''
    data_chunk=receiver.recv(buffer_size)
    while len(data_chunk) >= buffer_size:
        data_buffer+=data_chunk
        data_chunk=receiver.recv(buffer_size)
    data_buffer+=data_chunk
    return data_buffer


def receive(host='127.0.0.1', port=6969):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as receiver:
        receiver.connect((host, port))
        time.sleep(5.1)
        data_string =  recvall(receiver)
        data = pickle.loads(data_string)
        data.image.show()

if __name__ == "__main__":
    receive(host='27.5.107.136',port=6969)