"""
Script that informs you about being attacked.


wget https://raw.githubusercontent.com/Elvarg21/dragon/master/lab/first.py
naredi bitly iz linka!

"""

import signal
import time
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango
import cairo

WAIT_TIME = 0

class AttackWindow(Gtk.Window):

    def __init__(self):
        super(AttackWindow, self).__init__()

        self.setup()
        self.init_ui()

    def setup(self):
        self.set_app_paintable(True)
        self.set_type_hint(Gdk.WindowTypeHint.DOCK)
        self.set_keep_above(True)

        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual is not None and screen.is_composited():
            self.set_visual(visual)

    def init_ui(self):
        self.connect("draw", self.on_draw)

        lbl = Gtk.Label()
        text = "Roar! A dragon attacked your computer!"
        lbl.set_text(text)

        fd = Pango.FontDescription("Serif 40")
        lbl.modify_font(fd)
        lbl.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse("white"))

        self.add(lbl)

        #self.resize(300, 250)
        width, height = get_desktop_size()
        self.resize(width, height)
        #self.resize(1, 1)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_draw(self, wid, cr):
        #cr.set_operator(cairo.OPERATOR_CLEAR)
        cr.set_source_rgba(0, 0, 0, 1)
        cr.set_operator(cairo.OPERATOR_SOURCE)
        cr.paint()
        cr.set_operator(cairo.OPERATOR_OVER)


def get_desktop_size():
    root_window = Gdk.get_default_root_window()
    return root_window.get_width(), root_window.get_height()


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL) # this will allow you to cancel program with Ctrl-C
    time.sleep(WAIT_TIME)
    app = AttackWindow()
    Gtk.main()


if __name__ == "__main__":
    main()
