#!/usr/bin/env python3
# This file is placed in the Public Domain.
# pylint: disable=C,I,R,E0402


__author__ = "B.H.J. Thate <thatebhj@gmail.com>"
__version__ = 1


import sys
import traceback


from bsd.clients import Client
from bsd.command import command
from bsd.errored import Errors
from bsd.loggers import Logging
from bsd.message import parse
from bsd.objects import update
from bsd.scanner import scandir, importer
from bsd.runtime import Cfg


def cprint(txt):
    if "v" in Cfg.opts:
        print(txt)
        sys.stdout.flush()


Logging.raw = cprint


class CLI(Client):

    def announce(self, txt):
        pass

    def raw(self, txt):
        print(txt)
        sys.stdout.flush()


def main():
    cfg = parse(' '.join(sys.argv[1:]))
    update(Cfg, cfg)
    scandir("mod", importer, doall=True)
    cli = CLI()
    command(cli, Cfg.otxt)


def waiter():
    got = []
    for ex in Errors.errors:
        if not Cfg.silent:
            traceback.print_exception(type(ex), ex, ex.__traceback__)
        got.append(ex)
    for exc in got:
        Errors.errors.remove(exc)


if __name__ == "__main__":
    main()
    waiter()
