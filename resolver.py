class vendor_resolver:
    def __init__(self):
        self.oui_data = open("oui.txt")
        self.oui_dict = {}
        for line in self.oui_data.read().splitlines():
            try:
                if line[0] in "0123456789ABCDEF":
                    tmp = line.split("\t")
                    if tmp[0][-9:] == "(base 16)":
                        self.oui_dict[tmp[0][0:6]] = tmp[2]
            except IndexError:
                continue
        self.oui_data.close()

    def get_vendor(self, mac_address):
        oui = mac_address.split(":")[:3]
        oui_base16 = "".join(oui)
        return self.oui_dict[oui_base16]