import mapper, ui
from time import sleep
from os import system
from os import name as systemname

system('cls' if systemname == 'nt' else 'clear')

map = mapper.mapper()

map.start()
try:
    while True:
        ui.showTable(map.netmap,map.runningthread)
        command = ui.userinput()
        system('cls' if systemname == 'nt' else 'clear')
except KeyboardInterrupt:
    print("\nGood Bye.")
