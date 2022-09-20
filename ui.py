from multiprocessing import reduction
import sys
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, CYAN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\33[36m', '\033[0m'
BRIGHT_BLACK, BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_BLUE, BRIGHT_MAGENTA, BRIGHT_CYAN, BRIGHT_WHITE = '\u001b[30;1m', '\u001b[31;1m', '\u001b[32;1m', '\u001b[33;1m', '\u001b[34;1m', '\u001b[35;1m', '\u001b[36;1m', '\u001b[37;1m'

line = f"{BRIGHT_CYAN}+{BRIGHT_YELLOW}---------------------{BRIGHT_CYAN}+{BRIGHT_YELLOW}-------------------{BRIGHT_CYAN}+{BRIGHT_YELLOW}-----------------------{BRIGHT_CYAN}+"
row_names = f"{BRIGHT_YELLOW}|          {BRIGHT_GREEN}IP         {BRIGHT_YELLOW}|        {BRIGHT_GREEN}MAC        {BRIGHT_YELLOW}|        {BRIGHT_GREEN}VENDOR         {BRIGHT_YELLOW}|"
def addSpaces(n):
    r=""
    for i in range(n):
        r+=" "
    return r

def showTable(ips):
    sys.stdout.write(line + '\n')
    sys.stdout.write(row_names + '\n')
    sys.stdout.write(line + '\n')
    forget = 0
    for i in ips:
        new_line = f"{BRIGHT_YELLOW}| "
        forget+=1
        if forget>2:
            new_line += f"{BRIGHT_GREEN}[{BRIGHT_MAGENTA}{forget-2}{BRIGHT_GREEN}] {(BRIGHT_RED if ips['you']==i else BRIGHT_WHITE )}{i}"+addSpaces(16-len(i))+f"{BRIGHT_YELLOW}|" #adds ip format
            new_line += f" {BRIGHT_WHITE}{ips[i][0]} {BRIGHT_YELLOW}|" #adds mac adress
            new_line += f" {BRIGHT_WHITE}{ips[i][1]} {BRIGHT_YELLOW}"+addSpaces(21-len(ips[i][1]))+"|" #adds vendor
            print(new_line)
    sys.stdout.write(line + '\n')