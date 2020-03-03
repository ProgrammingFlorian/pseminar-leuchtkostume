# Sets up TCP Server under port 12345
# Automatically accepts first client
# Sends messages on GPIO Button press (13, 19, 26) with button id

import socket
import RPi.GPIO as GPIO
import time

client_exists = False

def create_server():
    host = "localhost"
    print(host)
    port = 12345

    s = socket.socket()
    s.bind((host, port))

    s.listen(10)

    return s


def accept_client(s):
    c, address = s.accept()
    print("Connected to: " + str(address))
    return c


def send_message(c, data):
    c.send(data.encode())


def setup_pins():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.add_event_detect(13, GPIO.RISING, callback=button_callback)
    GPIO.add_event_detect(19, GPIO.RISING, callback=button_callback)
    GPIO.add_event_detect(26, GPIO.RISING, callback=button_callback)


def button_callback(btn_id):
    print('btn ' + btn_id + ' pressed')
    send_message(conn, btn_id)


server = create_server()
setup_pins()
conn = accept_client(server)

while True:
    time.sleep(0.1)