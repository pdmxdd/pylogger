from time import sleep
from pynput import keyboard

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    sleep(30)
    listener.stop()
