import socket
from PIL import Image

HOST = '127.0.0.1'
PORT = 6969

def recvall(receiver, buffer_size=65536):
    '''
    receiver: socket
    buffer_size: int
    '''
    data_buffer = b''
    data_chunk = b''
    data_chunk=receiver.recv(buffer_size)
    while len(data_chunk) >= buffer_size:
        data_buffer+=data_chunk
        data_chunk=receiver.recv(buffer_size)
    data_buffer+=data_chunk
    return data_buffer
    
def join_image(images):
    pass 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as receiver:
    receiver.connect((HOST, PORT))
    print(receiver.recv(4096))
    pixel_data =  recvall(receiver)
    image = Image.frombytes("RGB", (2880 ,1800), pixel_data, 'raw')
    image.show()
