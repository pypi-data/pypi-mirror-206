from collections import namedtuple

__version__ = "0.4.0a1"


AioWorkers = namedtuple("AioWorkers", "plugins groups")
Groups = namedtuple("Groups", "include exclude")


class Plugins(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.default = False
