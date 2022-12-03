import network, socket
from secret import SSID, PASSWORD
from time import sleep
from machine import Pin

led = Pin("LED", Pin.OUT)

a = 0
b = 0
c = 0
d = 0
e = 0

html = """<!DOCTYPE html>
<html>
    <body> <h1>{a}|{b}|{c}|{d}|{e}</h1>
    </body>
</html>
""".format(a=a, b=b, c=c, d=d, e=e)

for i in range(0, 5):
    led.on()
    sleep(0.1)
    led.off()
    sleep(0.1)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

connectCount = 0

max_wait = 100
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    sleep(1)

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    led.on()
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(100)

print('listening on', addr)

# Listen for connections
while True:
    try:
        cl, addr = s.accept()
        print('client connected from', addr)
        request = cl.recv(1024)
        print(request)

        request = str(request)

        response = html

        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()

    except OSError as e:
       print('connection closed')