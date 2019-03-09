import socket
import struct
import time

from PIL import Image


def recvall(receiver, buffer_size=65536):
    data_buffer = b''
    data_chunk=receiver.recv(buffer_size)
    while len(data_chunk) >= buffer_size:
        data_buffer+=data_chunk
        data_chunk=receiver.recv(buffer_size)
    data_buffer+=data_chunk
    return data_buffer
    
def get_shape(sock):
    shape = sock.recv(64)
    shape = tuple(map(int,str(shape)[2:-1].split(',')))
    return shape 

def display(pixel_data,shape):
    image = Image.frombytes("RGB", shape, pixel_data, 'raw')
    image.show()

def join_image(image_parts):
    return ''.join(image_parts)

def receive(host='127.0.0.1', port=1300):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as receiver:
        receiver.connect((host, port))
        receiver.send(bytes('im ready','utf-8'))
        shape = get_shape(receiver)
        pixel_data =  recvall(receiver)
    return pixel_data,shape

if __name__ == "__main__":
    display(*receive())
