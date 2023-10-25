import sys
import tty
import termios 
from time import sleep

tty_attrs = termios.tcgetattr(0)
tty.setcbreak(0)

def run():
    while True: 
        ch = sys.stdin.read(1)
        if '1' <= ch <= '9':
            for _ in range(int(ch)):
                sys.stdout.buffer.write(b'\x07')
                sys.stdout.buffer.flush()
                sleep(1) 

try: 
    run()
finally: 
    termios.tcsetattr(0, termios.TCSADRAIN, tty_attrs)




