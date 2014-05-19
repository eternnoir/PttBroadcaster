# -*- coding: utf-8 -*-
import IrcBot

class IrcBroadcaster():

    def __init__(self, board, delayTime, channel, nickname, server, port=6667):
        self.ircbot = IrcBot.Bot(channel, nickname, server, port)
        self.board = board
        self.delayTime = delayTime

    def start(self):
        self.ircbot.start()
