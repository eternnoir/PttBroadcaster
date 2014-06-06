# -*- coding: utf-8 -*-
import IrcBot
from threading import Thread
from time import sleep
from PyrserPTT import PyserPtt

pttDomain = 'http://www.ptt.cc'

class IrcBroadcaster():

    def __init__(self, board, delayTime, channel, nickname, server, port=6667):
        self.ircbot = IrcBot.Bot(channel, nickname, server, port)
        self.board = board
        self.delayTime = delayTime
        self.channel = channel
        self.pttPyser = PyserPtt.PyserPtt(board,5)

    def start(self):
        self.botTread = Thread(target=self.ircbot.start)
        self.botTread.daemon = True
        self.botTread.start()
        sleep(20)
        print 'irc joined'
        self.postThread = Thread(target=self.doBroadcaster)
        self.postThread.daemon = True
        self.postThread.start()


    def doBroadcaster(self):
        while True:
            self.postNewArtical();
            sleep(self.delayTime);

    def postNewArtical(self):
        print 'get New Artical'
        articals = self.pttPyser.getNewArticals()
        for a in articals:
            url = pttDomain+a.url
            self.ircbot.say(a.title + '        < '
                            + url + ' >')
            sleep(1)
