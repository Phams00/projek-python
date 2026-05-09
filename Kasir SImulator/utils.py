import os
import time
import json

def clrscr():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input('tekan enter untuk melanjutkan...')

def wait(durasi):
    time.sleep(durasi)
