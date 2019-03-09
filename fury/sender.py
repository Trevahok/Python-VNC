from PIL import Image
import mss
import socket
import time
from data import SocketData
import pickle

def screenshot():
    with mss.mss() as sct:
        img = sct.grab(sct.monitors[1])
    return rgba_to_rgb(img)

def rgba_to_rgb(im):
    return Image.frombytes('RGB', im.size, im.bgra, 'raw', 'BGRX')

def transmit(image, host='127.0.0.1', port=6969):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sender:

        image = image.resize((1280, 720), Image.ANTIALIAS)

        data = SocketData(image=image)
        data_string = pickle.dumps(data)
        print(len(data_string))

        sender.bind((host, port))
        sender.listen()
        conn, addr = sender.accept()

        with conn:
            print('Connected by', addr)
            conn.sendall(data_string)

if __name__ == "__main__":
    transmit(screenshot())
    