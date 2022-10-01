import sys
from os import system
from os import name as systemname

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, CYAN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\33[36m', '\033[0m'
BRIGHT_BLACK, BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_BLUE, BRIGHT_MAGENTA, BRIGHT_CYAN, BRIGHT_WHITE = '\u001b[30;1m', '\u001b[31;1m', '\u001b[32;1m', '\u001b[33;1m', '\u001b[34;1m', '\u001b[35;1m', '\u001b[36;1m', '\u001b[37;1m'
# bright colors might not work on any terminals
line = f"{BRIGHT_CYAN}+{BRIGHT_YELLOW}---------------------{BRIGHT_CYAN}+{BRIGHT_YELLOW}-------------------{BRIGHT_CYAN}+{BRIGHT_YELLOW}-----------------------{BRIGHT_CYAN}+"
row_names = f"{BRIGHT_YELLOW}|          {BRIGHT_GREEN}IP         {BRIGHT_YELLOW}|        {BRIGHT_GREEN}MAC        {BRIGHT_YELLOW}|        {BRIGHT_GREEN}VENDOR         {BRIGHT_YELLOW}|"
end_table = f"{BRIGHT_CYAN}+{BRIGHT_YELLOW}-----------------------------------------------------------------{BRIGHT_CYAN}+"

def clear():
    system('cls' if systemname == 'nt' else 'clear')

def addSpaces(n):
    r=""
    for i in range(n):
        r+=" "
    return r

def showTable(ips,scandone=[]):
    sys.stdout.write(line + '\n')
    sys.stdout.write(row_names + '\n')
    sys.stdout.write(line + '\n')
    forget = 0
    for i in ips:
        new_line = f"{BRIGHT_YELLOW}| "
        forget+=1
        if forget>2:
            new_line += f"{BRIGHT_GREEN}[{BRIGHT_MAGENTA}{forget-2}{BRIGHT_GREEN}]{addSpaces(3-len(str(forget-2)))}{(BRIGHT_RED if ips['you']==i else (BRIGHT_MAGENTA if ips['gateway']==i else BRIGHT_WHITE) )}{i}"+addSpaces(15-len(i))+f"{BRIGHT_YELLOW}|" #adds ip format
            new_line += f" {BRIGHT_WHITE}{ips[i][0]} {BRIGHT_YELLOW}|" #adds mac adress
            new_line += f" {BRIGHT_WHITE}{ips[i][1]} {BRIGHT_YELLOW}"+addSpaces(21-len(ips[i][1]))+"|" #adds vendor
            print(new_line)
    sys.stdout.write(line + '\n')
    sys.stdout.write(f"{BRIGHT_YELLOW}| {BRIGHT_GREEN}SCAN{BRIGHT_WHITE}:")
    sys.stdout.write((" Running"+addSpaces(51) if len(scandone)!=0 else " Done"+addSpaces(54))+f"{BRIGHT_YELLOW}|\n")
    sys.stdout.write(f"{BRIGHT_YELLOW}| {BRIGHT_GREEN}RUNNING THREADS{BRIGHT_WHITE}: {len(scandone)}{addSpaces(47-len(str(len(scandone))))}{BRIGHT_YELLOW}|" + '\n')
    sys.stdout.write(end_table + '\n')
    sys.stdout.write(f"{BRIGHT_YELLOW}| {BRIGHT_RED}RED{BRIGHT_WHITE}: Your device                                                {BRIGHT_YELLOW}|" + '\n')
    sys.stdout.write(f"{BRIGHT_YELLOW}| {BRIGHT_MAGENTA}MAGENTA{BRIGHT_WHITE}: Your gateway                                           {BRIGHT_YELLOW}|" + '\n')
    sys.stdout.write(end_table + '\n')

def userinput():
    sys.stdout.write(f"{BRIGHT_YELLOW}> {BRIGHT_WHITE}")
    return input()

def showHelp():
    sys.stdout.write('Commands:\n')
    sys.stdout.write(f"{BRIGHT_GREEN}Rescan{BRIGHT_WHITE}: {BRIGHT_YELLOW}Initialise a new network scan.\n")
    sys.stdout.write(f"{BRIGHT_GREEN}Exit{BRIGHT_WHITE}: {BRIGHT_YELLOW}Stop the script.\n")
    sys.stdout.write(BRIGHT_WHITE)
    input("press enter to continue.")
    clear()


