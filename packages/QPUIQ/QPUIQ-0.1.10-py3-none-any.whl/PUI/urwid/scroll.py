from .. import *
from .base import *

class UListBox(UBase):
    def update(self, prev):
        if prev and hasattr(prev, "ui"):
            self.body = prev.body
            self.ui = prev.ui
        else:
            self.body = urwid.SimpleFocusListWalker([urwid.AttrMap(urwid.Text(""), None, "focus") ])
            self.ui = urwid.ListBox(self.body)

    def addChild(self, idx, child):
        if idx < len(self.body):
            self.body[idx] = child.ui
        else:
            self.body.append(child.ui)

    def removeChild(self, idx, child):
        if len(self.body)==1:
            self.body[0] = urwid.Text("")
        else:
            del self.body[idx]
