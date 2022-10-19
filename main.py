import ui
ui.uprint("Importing modules\n")

try:
    from os import geteuid #not windows friendly
    if geteuid() != 0:
        ui.uprint("You need to run this script as a root user.\n", char="!")
        exit()
except ImportError as e:
    ui.uprint("geteuid not possible, windows solutions comming soon\n", char="!")

import mapper, relay

map = mapper.mapper()
rel = relay.mitm()
selected = None
map.start()
ui.clear()

command = ""
try:
    while True:
        if command == "mitm":
            relay.IPForward_switch()
        elif command.isnumeric():
            ui.uprint("updating the informations.\n")
            rel.victim_ip, rel.victim_mac = map.get_info(int(command))
            rel.gateway_ip, rel.gateway_mac = map.get_gateway()
            selected = int(command)
            ui.clear()
        elif command == "rescan":
            map.start()
            ui.clear()
        elif command == "exit":
            print("\nGood Bye.")
            exit()
        elif command == "help":
            ui.showHelp()
        ui.showTable(map.netmap,map.runningthread,selected)
        command = ui.userinput()
        ui.clear()
except KeyboardInterrupt:
    print("\nGood Bye.")
