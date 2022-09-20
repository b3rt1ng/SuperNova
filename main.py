print("Importing modules")
import mapper, ui
from time import sleep
from os import system
from os import name as systemname

map = mapper.mapper()
map.start()

def clear():
    system('cls' if systemname == 'nt' else 'clear')

clear()
command = ""
try:
    while True:
        if command == "rescan":
            map.start()
            clear()
        elif command == "exit":
            print("\nGood Bye.")
            exit()
        ui.showTable(map.netmap,map.runningthread)
        command = ui.userinput()
        clear()
except KeyboardInterrupt:
    print("\nGood Bye.")
