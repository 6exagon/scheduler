'''
Sets up top menu bar on any system.
'''

import platform
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
import src.app

def setup(root):
    '''Sets up menu bar.'''
    filedict = [
        ('New', src.app.newdialog, 'N'),
        ('Open...', src.app.opendialog, 'O'),
        ('Save', src.app.save, 'S'),
        ('Save As...', src.app.saveas, None),
        ('Export as CSV', src.app.export, 'E'),
        ('Close', src.app.close, 'W')]
    editdict = [
        ('Undo', src.app.undo, 'Z'),
        ('Redo', src.app.redo, 'Y'),
        None,
        ('Cut', src.app.cut, 'X'),
        ('Copy', src.app.copy, 'C'),
        ('Paste', src.app.paste, 'V')]
    helpdict = [
        ('Help', src.app.helpmenu),
        ('About', src.app.about)]

    control = ('Ctrl+', '<Control-')
    if platform.system() == 'Darwin':
        control = ('Command+', '<Command-')
        del filedict[5]
        helpdict = ()
        root.createcommand('tkAboutDialog', src.app.about)
        root.createcommand('::tk::mac::ShowHelp', src.app.helpmenu)
        root.createcommand('::tk::mac::OpenDocument', src.app.open_file)
        root.createcommand('::tk::mac::Quit', src.app.close)

    menubar = tkinter.Menu(root)
    filemenu = tkinter.Menu(menubar, name='file', tearoff=0)
    for x in filedict:
        if x[2]:
            accel = control[0] + x[2]
            filemenu.add_command(label=x[0], command=x[1], accelerator=accel)
            root.bind_all(control[1] + x[2].lower() + '>', x[1])
        else:
            filemenu.add_command(label=x[0], command=x[1])
    menubar.add_cascade(label='File', menu=filemenu, underline=0)
    editmenu = tkinter.Menu(menubar, name='edit', tearoff=0)
    for x in editdict:
        if x:
            accel = control[0] + x[2]
            editmenu.add_command(label=x[0], command=x[1], accelerator=accel)
            root.bind_all(control[1] + x[2].lower() + '>', x[1])
        else:
            editmenu.add_separator()
    menubar.add_cascade(label='Edit', menu=editmenu, underline=0)
    helpmenu = tkinter.Menu(menubar, name='help', tearoff=0)
    for x in helpdict:
        helpmenu.add_command(label=x[0], command=x[1])
    menubar.add_cascade(label='Help', menu=helpmenu, underline=0)
    root.config(menu=menubar)
