import ui
ui.uprint("Importing modules")

try:
    from os import geteuid #not windows friendly
    if geteuid() != 0:
        ui.uprint("You need to run this script as a root user.", char="!")
        exit()
except ImportError as e:
    ui.uprint("geteuid not possible, windows solutions comming soon", char="!")

import mapper, relay

map = mapper.mapper()
rel = relay.mitm()
selected = None
map.start()
ui.clear()

command = ""
try:
    while True:
        match command:
            case "help":
                ui.showHelp()
            case "exit":
                ui.uprint("Goodbye", char="*")
                exit()
            case "rescan":
                map.start()
            case "mitm":
                rel.start()
            

        if command.isnumeric(): #ugly
            ui.uprint("updating the informations.")
            rel.victim_ip, rel.victim_mac = map.get_info(int(command))
            rel.gateway_ip, rel.gateway_mac = map.get_gateway()
            selected = int(command)
        ui.showTable(map.netmap,map.runningthread,selected)
        command = ui.userinput()
        ui.clear()
except KeyboardInterrupt:
    print()
    ui.uprint("GoodBye.", char="*")
