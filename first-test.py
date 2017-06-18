import socket
HOST = '192.168.0.200'
PORT = 1234
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
send = sock.send

def pixel(x,y,r,g,b,a=255):
    if a == 255:
        send('PX %d %d %02x%02x%02x\n' % (x,y,r,g,b))
    else:
        send('PX %d %d %02x%02x%02x%02x\n' % (x,y,r,g,b,a))

def bigpixel(x,y,m,r,g,b,a=255):
    for i in xrange(x-m,x+m):
        for j in xrange(y-m,y+m):
            if a == 255:
                send('PX %d %d %02x%02x%02x\n' % (i,j,r,g,b))
            else:
                send('PX %d %d %02x%02x%02x%02x\n' % (i,j,r,g,b,a))

def rect(x,y,w,h,r,g,b):
    for i in xrange(x,x+w):
        for j in xrange(y,y+h):
            pixel(i,j,r,g,b)
            
import random  
def worm(x,y,n,r,g,b):
    while n:
        pixel(x,y,r,g,b,25)
        x += random.randint(0,2)-1
        y += random.randint(0,2)-1
        n -= 1

def image(path):
    from PIL import Image
    im = Image.open(path).convert('RGB')
    im.thumbnail((480, 640), Image.ANTIALIAS)
    _,_,w,h = im.getbbox()  
    for x in xrange(w):
        for y in xrange(h):
            r,g,b = im.getpixel((x,y))
            pixel(x,y,r,g,b)


worm(400, 300, 100000, 255, 255, 255)
#image('image.JPG')
