'''
Main entry point of program, handles code at top level.
'''

import os
try:
    import tkinter
    from tkinter import filedialog
except ImportError:
    import Tkinter as tkinter
    import tkFileDialog as filedialog
import src.schedule
import src.menusetup

def newdialog(evt=None):
    pass

def opendialog(evt=None):
    '''Calls open_file with filename chosen by file dialog.'''
    open_file(filedialog.askopenfilename())

def save(evt=None):
    pass

def saveas(evt=None):
    pass

def export(evt=None):
    pass

def close(evt=None):
    '''Closes program.'''
    raise SystemExit

def undo(evt=None):
    pass

def redo(evt=None):
    pass

def cut(evt=None):
    pass

def copy(evt=None):
    pass

def paste(evt=None):
    pass

def helpmenu(evt=None):
    pass

def about(evt=None):
    pass

def open_file(*files):
    '''Called either by macOS or opendialog, opens any number of files.'''
    for x in files:
        print(x)

def main(resource_path):
    '''Called when package is run.'''
    t = tkinter.Tk()
    src.menusetup.setup(t)
    loadf = open(os.path.join(resource_path, 'version.txt'), 'r')
    t.title('Scheduler ' + loadf.readline())
    loadf.close()
    t.resizable(0, 0)
    canvas = tkinter.Canvas(t, width=260, height=260, bg='#ddd')
    canvas.pack()
    filepath = os.path.join(resource_path, 'images', 'icon.gif')
    img = tkinter.PhotoImage(file=filepath)
    canvas.create_image(130, 130, image=img, anchor='center')
    t.mainloop()
