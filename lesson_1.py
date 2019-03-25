import os
import time

def show(command):
    print('接下来要演示的指令是：' + command)
    wait = input()
    ans = os.system(command)
    print('\n')


def send_queue(*args):
    for command in args:
        show(command)

def default_show(*args):
    fist_command = args[0]
    show(fist_command)
    for command in args[1:]:
        whole_command = fist_command + ' ' + command
        show(whole_command)

if __name__ == '__main__':
    #default_show('cal','-jy','-j')
    default_show('who', '-- h', '-d','-l','-m','-p')
    #default_show('finger', '-jy', '-j')

    # send_queue('cal','cal -jy','cal -j')
    # send_queue('who','who -jy','cal -j')
    # show('cal')
    # show('cal -jy')
    # show('cal -j')



