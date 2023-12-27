from flask import Flask
from pynput import keyboard, mouse
import socket
import time

app = Flask(__name__)
kb = keyboard.Controller()
m = mouse.Controller()
DELAY = 0.1
EP_POS = (858, 497) # play button coords
get_ip = lambda: socket.gethostbyname(socket.gethostname())

def start_episode():
    for i in range(19):
        kb.press(keyboard.Key.tab)
        kb.release(keyboard.Key.tab)
        time.sleep(DELAY)
    time.sleep(1.5)
    kb.press(keyboard.Key.enter)
    kb.release(keyboard.Key.enter)
    time.sleep(5)
    kb.type('f')

def next_episode():
    kb.type('f')
    for i in range(12):
        time.sleep(DELAY)
        kb.press(keyboard.Key.tab)
        kb.release(keyboard.Key.tab)
    time.sleep(1)
    m.position = EP_POS
    m.click(mouse.Button.left)

@app.route('/')
def app_index():
    return 'use /start or /next. also /type/<keys> and /refresh'

@app.route('/start')
def app_start():
    start_episode()
    return 'started'

@app.route('/next')
def app_next():
    next_episode()
    return 'next'

@app.route('/type/<string:keys>')
def app_type(keys):
    kb.type(keys)
    return 'typed'

@app.route('/refresh')
def app_refresh():
    kb.press(keyboard.Key.ctrl)
    kb.press('r')
    time.sleep(DELAY)
    kb.release('r')
    kb.release(keyboard.Key.ctrl)
    return 'refreshed'

if __name__ == '__main__':
    print('Server running at http://{}:8080'.format(get_ip()))
    app.run(host='0.0.0.0', port=8080)