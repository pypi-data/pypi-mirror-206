from .. import *
from .base import *
from tkinter.scrolledtext import ScrolledText

class TkScroll(TkBaseWidget):
    def update(self, prev):
        if prev and hasattr(prev, "ui"):
            self.ui = prev.ui
        else:
            self.ui = ScrolledText(self.tkparent.ui, state='disable')
            self.ui.grid(row=0, column=0, sticky='nsew')

    def addChild(self, idx, child):
        self.ui.window_create('1.0', window=child.ui)
        child.ui.bind('<Button-4>', lambda event: self.ui.yview_scroll(-1, tk.UNITS))
        child.ui.bind('<Button-5>', lambda event: self.ui.yview_scroll( 1, tk.UNITS))

    def removeChild(self, idx, child):
        self.ui.delete('1.0', tk.END)