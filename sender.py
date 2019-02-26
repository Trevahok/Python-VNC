from PIL import Image
import mss
import socket

HOST = '127.0.0.1'
PORT = 6969

def pil_from_bytes(im):
    img_from_bytes = Image.frombytes('RGB', im.size, im.bgra, 'raw', 'BGRX')
    return img_from_bytes.tobytes()

def split_image(image, parts=2):
    '''

    Input: 
        image: Bytes 
    Output: 
        image_parts: List

    '''
    size = len(image)


with mss.mss() as sct:
    im = sct.grab(sct.monitors[1])
    rgb = pil_from_bytes(im)
    shape = f'{im.width},{im.height}'

print(im.width, im.height)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sender:
    sender.bind((HOST, PORT))
    sender.listen()
    conn, addr = sender.accept()
    with conn:
        conn.send(bytes(shape,'utf-8'))
        print('Connected by', addr)
        conn.sendall(rgb)

