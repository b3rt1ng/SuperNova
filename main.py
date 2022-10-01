print("Importing modules")
import mapper, ui
from time import sleep

map = mapper.mapper()
map.start()
ui.clear()

command = ""
try:
    while True:
        if command == "rescan":
            map.start()
            ui.clear()
        elif command == "exit":
            print("\nGood Bye.")
            exit()
        elif command == "help":
            ui.showHelp()
        ui.showTable(map.netmap,map.runningthread)
        command = ui.userinput()
        ui.clear()
except KeyboardInterrupt:
    print("\nGood Bye.")
