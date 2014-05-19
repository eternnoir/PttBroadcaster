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
        self.channel = channel

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.join(self.channel)

    def say(self, c, msg):
        c.privmsg(self.channel, msg)

    def sayTo(self, c, user, msg):
        tomsg = user+': '+msg
        self.say(c, tomsg)

    def notice(self, c, noticeId, msg):
        c.notice(noticeId, msg)



