from time import sleep
from pynput import keyboard

log = []

def on_press(key):
    special_lookup = {
        "Key.space": " ",
        "Key.tab": " "
    }
    try:
        log.append(key.char)
    except AttributeError:
        if str(key) in special_lookup.keys():
            log.append(special_lookup[str(key)])

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    sleep(10)
    listener.stop()
    print("".join(log))
