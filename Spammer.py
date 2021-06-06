import os
import pyautogui
from time import sleep
import sys

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

def heading():
    spaces = " " * 76
    sys.stdout.write(RED + spaces + """
      ██████  ██▓███   ▄▄▄       ███▄ ▄███▓ ███▄ ▄███▓▓█████  ██▀███  
    ▒██    ▒ ▓██░  ██▒▒████▄    ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒▓█   ▀ ▓██ ▒ ██▒
    ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄  ▓██    ▓██░▓██    ▓██░▒███   ▓██ ░▄█ ▒
      ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██    ▒██ ▒██    ▒██ ▒▓█  ▄ ▒██▀▀█▄  
    ▒██████▒▒▒██▒ ░  ░ ▓█   ▓██▒▒██▒   ░██▒▒██▒   ░██▒░▒████▒░██▓ ▒██▒
    ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒░   ░  ░░ ▒░   ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░
    ░ ░▒  ░ ░░▒ ░       ▒   ▒▒ ░░  ░      ░░  ░      ░ ░ ░  ░  ░▒ ░ ▒░
    ░  ░  ░  ░░         ░   ▒   ░      ░   ░      ░      ░     ░░   ░ 
          ░                 ░  ░       ░          ░      ░  ░   ░   
    """ + END + BLUE +
    '\n' + '{}Spam your friends ({}Spammer{}){}'.format(YELLOW, RED, YELLOW, BLUE).center(98) +
    '\n' + 'Made by: {0}Kevin Carvalho ({1}kw4z{2})'.format(YELLOW, RED, YELLOW, BLUE).center(93) +
    '\n' + 'Version: {}1.0{}\n'.format(YELLOW, END).center(86))


# script's optionBanner function
def optionBanner():
    print("\n---------------------------------------------------------------------------")
    print("\n\t*+-+-+-+-+-+-+* {}Welcome to the {}Spammer.py {}*+-+-+-+-+-+-+*\n".format(BLUE, YELLOW, WHITE))
    print("---------------------------------------------------------------------------\n")
    print('\n{}[{}+{}]{} Choose an option from the menu :\n'.format(BLUE, YELLOW, BLUE, WHITE))
    sleep(0.2)
    print('\t{}[{}1{}]{} Spamming from clipboard '.format(BLUE, YELLOW, BLUE, WHITE))
    sleep(0.2)
    print('\t{}[{}2{}]{} Spamming from variable text '.format(BLUE, YELLOW, BLUE, WHITE))
    sleep(0.2)
    print('\n\t{}[{}E{}]{} Exit G2S2 Spammer\n'.format(BLUE, YELLOW, BLUE, WHITE))

# script's numberBanner function
def numberBanner():
    print('\n{}[{}+{}]{} Choose a number of messages for you spam :\n'.format(BLUE, YELLOW, BLUE, WHITE))
    sleep(0.2)
    print('\t{}[{}1{}]{} 15 messages'.format(YELLOW, RED, YELLOW, WHITE))
    sleep(0.2)
    print('\t{}[{}2{}]{} 30 messages'.format(YELLOW, RED, YELLOW, WHITE))
    sleep(0.2)
    print('\t{}[{}3{}]{} 120 messages'.format(YELLOW, RED, YELLOW, WHITE))
    sleep(0.2)
    print('\t{}[{}4{}]{} Custom number '.format(YELLOW, RED, YELLOW, WHITE))
    sleep(0.2)
    print('\n\t{}[{}E{}]{} Exit G2S2 Spam\n'.format(YELLOW, RED, YELLOW, WHITE))

# script for asking how many messages for variablespam
def variableSpam():
    numberBanner()
    ans = ""
    number = ""
    ans = input("\n{}[{}>{}]{} Please intert option: ".format(BLUE, YELLOW, BLUE, WHITE))
    spamtext = ""
    if ans == "1":
        print("\n{}You choosed {}15 messages{} option.{}".format(YELLOW, RED, YELLOW, WHITE))
        variableScript(15)
    elif ans == "2":
        print("\n{}You choosed {}30 messages{} option.{}".format(YELLOW, RED, YELLOW, WHITE))
        variableScript(30)
    elif ans == "3":
        print("\n{}You choosed {}120 messages{} option.{}".format(YELLOW, RED, YELLOW, WHITE))
        variableScript(120)
    elif ans == "4":
        print("\n{}You choosed {}custom number{} option.{}".format(YELLOW, RED, YELLOW, WHITE))
        number = input("\n{}[{}>{}]{} Number of messages you want to send: ".format(BLUE, YELLOW, BLUE, WHITE))
        variableScript(int(number))
    elif ans == "E":
        os._exit(0)
    else:
        print("{}\n[-] Invalid option{}\n".format(RED, WHITE))
        variableSpam()

# script for spamming from variable
def variableScript(sec:int):
    text = ""
    text = input("\n{}[{}>{}]{} Type the text you want to spam: ".format(BLUE, YELLOW, BLUE, WHITE))
    pyautogui.alert("Spammer starting in 3 seconds after clicking 'ok'")
    sleep(3)
    for i in range (sec):
        pyautogui.write(text)
        pyautogui.hotkey('enter') # enter key
        sleep(1)


# script for asking how many messages for clipspam
def clipSpam():
    numberBanner()
    ans = ""
    ans = input("\n{}[{}>{}]{} Please intert option: ".format(BLUE, YELLOW, BLUE, WHITE))
    if ans == "1":
        print("\n{}You choosed {}15 messages{} option.{}".format(YELLOW, RED, YELLOW, WHITE))
        clipScript(15)
    elif ans == "2":
        print("\n{}You choosed {}30 messages{} option.{}".format(YELLOW, RED, YELLOW, WHITE))
        clipScript(30)
    elif ans == "3":
        print("\n{}You choosed {}120 messages{} option.{}".format(YELLOW, RED, YELLOW, WHITE))
        clipScript(120)
    elif ans == "4":
        print("\n{}You choosed {}custom number{} option.{}".format(YELLOW, RED, YELLOW, WHITE))
        number = input("\n{}[{}>{}]{} Number of messages you want to send: ".format(BLUE, YELLOW, BLUE, WHITE))
        clipScript(int(number))
    elif ans == "E":
        os._exit(0)
    else:
        print("{}\n[-] Invalid option{}\n".format(RED, WHITE))
        clipSpam()

# script for spamming from clipboard
def clipScript(sec:int):
    pyautogui.alert("Spamming will start in 3 seconds after clicking 'OK'")
    sleep(3)
    for i in range (sec):
        pyautogui.hotkey('ctrl', 'v')  # ctrl-v to paste
        pyautogui.hotkey('enter') # enter key
        sleep(1)
    
def endMessage():
    print("\n{}kw4z {}thanks you for using {}Spammer.py!{}\n".format(RED, YELLOW, RED, WHITE))

# script's main function
def main():
    answ=True
    while answ:
        heading()
        optionBanner()
        ans = ""
        ans = input("\n{}[{}>{}]{} Please intert option: ".format(BLUE, YELLOW, BLUE, WHITE))
        if ans == "1":
            clipSpam()
        elif ans == "2":
            variableSpam()
        elif ans == "E":
            os._exit(0)
        else:
            print("{}\n[-] Invalid option{}\n".format(RED, WHITE))
            main()
        endMessage()   
main()
