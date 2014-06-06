# -*- coding: utf-8 -*-
from PttBroadcaster import IrcBroadcaster
from time import sleep

""" Example
board = 'Gossiping'
waitTime = 30
channel = '#PTT-GOS-NEWS'
nickName = 'PTTGOSBOT'
server = 'chat.freenode.net'
"""

board = ''
waitTime = 30
channel = ''
nickName = ''
server = ''



def main():
    caster = IrcBroadcaster.IrcBroadcaster(board,waitTime,channel,nickName,server)
    caster.start()
    while True:
        sleep(10)

if __name__ == '__main__':
    main()
