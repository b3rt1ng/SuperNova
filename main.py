import mapper, ui
from time import sleep

map = mapper.mapper()

map.start()
ui.showTable(map.netmap)

