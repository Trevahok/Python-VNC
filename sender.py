from PIL import Image
import mss
import socket

HOST = '127.0.0.1'
PORT = 6969

def pil_frombytes(im):
    img_from_bytes = Image.frombytes('RGB', im.size, im.bgra, 'raw', 'BGRX')
    return img_from_bytes.tobytes()

def split_image(image, parts=2):
    pass


with mss.mss() as sct:
    im = sct.grab(sct.monitors[1])

print(im.width, im.height)
rgb = pil_frombytes(im)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sender:
    sender.bind((HOST, PORT))
    sender.listen()
    conn, addr = sender.accept()
    with conn:
        print('Connected by', addr)
        conn.sendall(rgb)

