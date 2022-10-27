import sys
from os import system
from os import name as systemname

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, CYAN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\33[36m', '\033[0m'
BRIGHT_BLACK, BRIGHT_RED, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_BLUE, BRIGHT_MAGENTA, BRIGHT_CYAN, BRIGHT_WHITE = '\u001b[30;1m', '\u001b[31;1m', '\u001b[32;1m', '\u001b[33;1m', '\u001b[34;1m', '\u001b[35;1m', '\u001b[36;1m', '\u001b[37;1m'
# bright colors might not work on every terminals
line = f"{BRIGHT_CYAN}+{BRIGHT_YELLOW}---------------------{BRIGHT_CYAN}+{BRIGHT_YELLOW}-------------------{BRIGHT_CYAN}+{BRIGHT_YELLOW}-----------------------{BRIGHT_CYAN}+"
row_names = f"{BRIGHT_YELLOW}|          {BRIGHT_GREEN}IP         {BRIGHT_YELLOW}|        {BRIGHT_GREEN}MAC        {BRIGHT_YELLOW}|        {BRIGHT_GREEN}VENDOR         {BRIGHT_YELLOW}|"
end_table = f"{BRIGHT_CYAN}+{BRIGHT_YELLOW}-----------------------------------------------------------------{BRIGHT_CYAN}+"
chartable = {
    "+" : BRIGHT_GREEN,
    "!" : BRIGHT_RED,
    "-" : BRIGHT_YELLOW,
    "?" : BRIGHT_BLUE,
    "*" : BRIGHT_MAGENTA,
    "#" : BRIGHT_CYAN,
    "@" : BRIGHT_WHITE
}

def uprint(text, color=BRIGHT_WHITE, char="+", end="\n", same_line=False):
    if same_line:
        sys.stdout.write(f"\r{BRIGHT_BLUE}[{BRIGHT_GREEN}"+chartable[char]+f"{char}{BRIGHT_BLUE}]{color} {text}")
    else:
        sys.stdout.write(f"{BRIGHT_BLUE}[{BRIGHT_GREEN}"+chartable[char]+f"{char}{BRIGHT_BLUE}]{color} {text}{end}")
    (input("Press enter to continue") if char=="!" else None)

def clear():
    system('cls' if systemname == 'nt' else 'clear')

def addSpaces(n):
    r=""
    for i in range(n):
        r+=" "
    return r

def cut(n,text):
    print(text)
    while len(text)>=n:
        print(text)
        text=text[:-1]
    return text

def showTable(ips,scandone=[],sel=None):
    clear()
    sys.stdout.write(line + '\n')
    sys.stdout.write(row_names + '\n')
    sys.stdout.write(line + '\n')
    forget = 0
    for i in ips:
        new_line = f"{BRIGHT_YELLOW}| "
        forget+=1
        if forget>2:
            new_line += f"{BRIGHT_GREEN}["+(BRIGHT_CYAN if forget-2==sel else BRIGHT_MAGENTA)+f"{forget-2}{BRIGHT_GREEN}]{addSpaces(3-len(str(forget-2)))}{(BRIGHT_RED if ips['you']==i else (BRIGHT_MAGENTA if ips['gateway']==i else BRIGHT_WHITE) )}{i}"+addSpaces(15-len(i))+f"{BRIGHT_YELLOW}|" #adds ip format
            new_line += f" {BRIGHT_WHITE}{ips[i][0]} {BRIGHT_YELLOW}|" #adds mac adress
            new_line += f" {BRIGHT_WHITE}"+ips[i][1].ljust(22).replace("\n","")[:21]+f" {BRIGHT_YELLOW}|" #adds vendor
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
    sys.stdout.write(f"{BRIGHT_GREEN}mitm{BRIGHT_WHITE}: {BRIGHT_YELLOW}Will attempt an mitm attack on your selected victim.\n")
    sys.stdout.write(f"{BRIGHT_GREEN}Any numeric value{BRIGHT_WHITE}: {BRIGHT_YELLOW}Will select a target for the MITM attack.\n")
    sys.stdout.write(BRIGHT_WHITE)
    input("Press enter to continue.")
    clear()


