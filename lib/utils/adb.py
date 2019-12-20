#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.utils.shell import Shell


class Adb(Shell):
    def __init__(self, serial=""):
        self.serial = serial
        # if we are root shell
        self.is_root = False

    @classmethod
    def start_server(cls):
        return cls.cmd_and_debug('adb start-server')

    def root(self):
        ret = self.cmd_and_debug('adb -s "{}" root'.format(self.serial))
        if not 'cannot run as root' in ret['out']:
            self.is_root = True
        return ret

    def unsafe_shell(self, command, root=False):
        return self.cmd_and_debug(r'''adb -s "{}" shell "{}{}"'''.format(
            self.serial, 'su - -c ' if root and not self.is_root else '', command))

    def push(self, src, dst):
        return self.cmd_and_debug('adb -s "{}" push "{}" "{}"'.format(self.serial, src, dst))

    def reverse(self, port):
        return self.cmd_and_debug('adb -s "{0}" reverse tcp:{1} tcp:{1}'.format(self.serial, port))
