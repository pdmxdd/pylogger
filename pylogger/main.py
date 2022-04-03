from time import sleep
from pynput import keyboard

def on_press(key):
    try:
        print(key.char)
    except AttributeError:
        pass 

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    sleep(10)
    listener.stop()
