import keyboard as key, time
from colorama import init, Fore, Style

##Language: RUS
##ideaRivel -- code author.
##Date: 9.12.23 -- 14.12.23. Happy Hew Year!

def send_start_message():
    """Send start message and logotype"""

    print(Fore.BLUE + '``¶¶¶¶¶``¶¶¶¶¶¶`¶¶``¶¶`¶¶¶¶¶`¶¶````````¶¶``¶¶``¶¶¶¶``')
    print(Fore.BLUE + '``¶¶``¶¶```¶¶```¶¶``¶¶`¶¶````¶¶````````¶¶``¶¶`¶```¶¶``')
    print(Fore.BLUE + '``¶¶¶¶¶````¶¶```¶¶``¶¶`¶¶¶¶``¶¶````````¶¶``¶¶```¶¶¶``')
    print(Fore.BLUE + '``¶¶``¶¶```¶¶````¶¶¶¶``¶¶````¶¶`````````¶¶¶¶``¶```¶¶``')
    print(Fore.BLUE + '``¶¶``¶¶`¶¶¶¶¶¶```¶¶```¶¶¶¶¶`¶¶¶¶¶¶``````¶¶````¶¶¶¶``') 
    
    time.sleep(1)

    print(Style.RESET_ALL)
    print('RIVEL V3 -- это OpenSource анти-AFK бот для различных игр, за который нереально поулчить бан от античит-программы. Windows 10+')
    print('Made by', Fore.RED + 'idearivel', Fore.WHITE + '(Discord)')
send_start_message() 


def send_guide():
    """Send guide text"""
    
    time.sleep(1.5)
    print(Fore.BLUE + '=====================================================')
    print(Fore.BLUE+'Как использовать:', Fore.WHITE + '«walking» - способ движения. При способе движения, по нажатию клавиши CTRL бот будет немного двигаться с интервалом в 1 секунду, пока вы не нажмете ALT.', Fore.RED + 'Остановка бота может не произойти с первого раза! Нажимайте ALT несколько раз.')
    print(Fore.BLUE + '=====================================================')
    print(Style.RESET_ALL)
    time.sleep(3)
    print('Нажмите клавишу', Fore.BLUE + 'CTRL')
    print(Style.RESET_ALL)
send_guide()


def stop_bot_check():
    """Stop function"""

    print(Fore.BLUE + 'Бот приостановлен')
    print(Style.RESET_ALL)
    
    global inf
    inf = int(input('Чтобы возобновить работу бота, введите цифру "1" и нажмите CTRL: '))
    print(Style.RESET_ALL)

    if inf == 1:
         walking()

def walking():
    """Walking function"""
    
    inf = 1
    while inf == 1:
            if key.is_pressed('alt'):
                 stop_bot_check()
            key.press('w')
            time.sleep(1)
            if key.is_pressed('alt'):
                 stop_bot_check()
            key.release('w')
            time.sleep(1)
            if key.is_pressed('alt'):
                 stop_bot_check()
            key.press('s')
            time.sleep(1)
            if key.is_pressed('alt'):
                 stop_bot_check()
            key.release('s')
            time.sleep(1)
            if key.is_pressed('alt'):
                 stop_bot_check()
                 
key.add_hotkey('ctrl', walking)

key.wait() 

##Made by idearivel (Author's Discord) -- 2023