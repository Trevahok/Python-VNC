from PIL import Image
import mss
import socket

def screenshot():
    with mss.mss() as sct:
        im = sct.grab(sct.monitors[1])
    return  im

def rgba_to_rgb(im):
    return Image.frombytes('RGB', im.size, im.bgra, 'raw', 'BGRX')

def image_to_bytes(image):
    rgb = rgba_to_rgb(image)
    return rgb.tobytes()

def shape_to_string(im):
    return f'{im.width},{im.height}'

def split_image(image, parts=2):
    k, m = divmod(len(image),parts)
    return (image[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(parts))


def transmit(image,host='127.0.0.1',port=6969):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sender:
        sender.bind((host, port))
        sender.listen()
        conn, addr = sender.accept()
        shape = shape_to_string(image)
        pixel_data = image_to_bytes(image)
        with conn:
            conn.send(bytes(shape,'utf-8'))
            print('Connected by', addr)
            print('port1 is being used ')
            conn.sendall(pixel_data)
            print('port1 is  done being used ')

if __name__ == "__main__":
    image = screenshot()
    transmit(image)
    transmit(image, port=6970)
    