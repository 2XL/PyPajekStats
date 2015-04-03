#!/usr/bin/python

# simple.py

import pygtk
pygtk.require('2.0')
import gtk

class Simple:

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        win = gtk.Window(gtk.WINDOW_TOPLEVEL)

        win.connect("destroy", self.destroy)

        win.set_title("Simple")
        win.set_position(gtk.WIN_POS_CENTER)
        win.show_all()

Simple()
gtk.main()