# -*- coding: utf-8 -*-
import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr
from threading import *


class Bot(irc.bot.SingleServerIRCBot):

    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(
            self, [
                (server, port)], nickname, nickname)
        self.controler = bandonControl(self, channel)
        self.channel = channel

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.join(self.channel)

        print e.source.nick
        print e.arguments[0]
        #self.do_command(e, e.arguments[0])

        user = e.source.nick
        print e.arguments[0]
        a = e.arguments[0].split(":", 1)
        if len(a) > 1 and irc.strings.lower(a[0]) == irc.strings.lower(self.connection.get_nickname()):
            rmsg = irc.strings.lower(a[1]).strip()
            try:
                if len(rmsg.split(' ')) > 1:
                    command = rmsg.split(' ')[0]
                    msg = rmsg.split(' ')[1]
                else:
                    command = rmsg
                    msg = ''
                self.controler.doCommand(
                    c,
                    user,
                    irc.strings.lower(command).strip(),
                    msg)
            except:
                self.sayTo(c, user, u'Command Error')
        return

    def say(self, c, msg):
        c.privmsg(self.channel, msg)

    def sayTo(self, c, user, msg):
        tomsg = user+': '+msg
        self.say(c, tomsg)

    def notice(self, c, noticeId, msg):
        c.notice(noticeId, msg)


class IrcBroadcaster():

    def __init__(self, channel, nickname, server, port=6667, board, delayTime):
        self.ircbot = Bot(channel, nickname, server, port)
        self.board = board
        self.delayTime = delayTime
