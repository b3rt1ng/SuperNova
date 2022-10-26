import ui
from os import name as systemname
ui.uprint("Importing modules")

match systemname:
    case "nt":
        import ctypes
        su_rights = (ctypes.windll.shell32.IsUserAnAdmin() != 0)
    case "posix":
        from os import geteuid
        su_rights = (geteuid() == 0)
    case _:
        su_rights = True
        ui.uprint("Unknown OS, make sure you are running this script as a superuser", char="!")

if su_rights == False:
    ui.uprint("You need to run this script as a root user.", char="!")
    exit()

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
