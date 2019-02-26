import socket
from PIL import Image

HOST = '127.0.0.1'
PORT = 6969

def recvall(receiver, buffer_size=65536):
    '''
    Input: 
        receiver: socket
        buffer_size: int
    Output: 
        data_buffer: bytes
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
    shape = receiver.recv(4096)
    print(shape)
    shape = tuple(map(int,str(shape)[2:-1].split(',')))
    pixel_data =  recvall(receiver)
    image = Image.frombytes("RGB", shape, pixel_data, 'raw')
    image.show()
