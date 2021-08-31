'''
Main entry point of program, handles code at top level.
'''

import os
import webbrowser
try:
    import tkinter
    from tkinter import ttk
    from tkinter import filedialog
    from tkinter import messagebox
except ImportError:
    import Tkinter as tkinter
    import ttk
    import tkFileDialog as filedialog
    import tkMessageBox as messagebox
import src.schedule
import src.menusetup

schedule = src.schedule.Schedule()

def newdialog(evt=None):
    pass

def opendialog(evt=None):
    '''Calls open_file with filename chosen by file dialog.'''
    open_file(filedialog.askopenfilename(filetypes = [('Schedule','*.schd')]))

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
    '''Directs user to repository webpage.'''
    webbrowser.open('https://github.com/6exagon/scheduler/')

def about(evt=None):
    '''Reads version number and then creates About window.'''
    loadf = open(os.path.join(resource_path, 'version.txt'), 'r')
    text = 'Scheduler ' + loadf.readline() + '\nCreated by 6exagon'
    loadf.close()
    messagebox.showinfo('About Scheduler', text)

def open_file(*files):
    '''Called either by macOS or opendialog, opens and saves first filename.'''
    global schedule
    try:
        schedule = src.schedule.Schedule(files[0])
    except:
        messagebox.showerror('', 'Unable to read file.')
    if len(files) > 1:
        messagebox.showerror('', 'Cannot open more than one file at once.')

def main(res_path):
    '''Called when package is run.'''
    global resource_path
    resource_path = res_path
    t = tkinter.Tk()
    imgpath = os.path.join(resource_path, 'images', 'icon.gif')
    img = tkinter.PhotoImage(file=imgpath)
    t.call('wm', 'iconphoto', t._w, img)
    t.title('Scheduler')
    t.resizable(0, 0)
    src.menusetup.setup(t)
    canvas = tkinter.Canvas(t, width=260, height=260, bg='#ddd')
    canvas.pack()
    canvas.create_image(130, 130, image=img, anchor='center')
    t.mainloop()
