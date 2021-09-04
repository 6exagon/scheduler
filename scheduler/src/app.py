'''
Main entry point of program, handles code at top level.
'''

import os
import webbrowser
import platform
import sys
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
import src.panels

def newdialog(evt=None):
    '''Clears schedule.'''
    global schedule
    if save_continue():
        schedule = src.schedule.Schedule()

def opendialog(evt=None):
    '''Calls open_file with filename chosen by file dialog.'''
    open_file(filedialog.askopenfilename(filetypes = [('Schedule','*.schd')]))

def save(evt=None):
    '''Serializes schedule, or calls saveas if schedule has no filename.'''
    if schedule.filename:
        schedule.serialize()
    else:
        saveas()

def saveas(evt=None):
    '''Saves schedule under new filename.'''
    filename = filedialog.asksaveasfilename(
        defaultextension='.schd',
        filetypes=[('Schedule', '*.schd')])
    if len(filename):
        schedule.filename = filename
        save()

def export(evt=None):
    pass

def close(evt=None):
    '''Closes program after save prompt.'''
    if save_continue():
        t.destroy()

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
    '''Called either by macOS or opendialog, opens first filename.'''
    global schedule
    if save_continue() and len(files[0]):
        try:
            schedule = src.schedule.Schedule(files[0])
        except:
            messagebox.showerror('', 'Unable to read file.')
        if len(files) > 1:
            messagebox.showerror('', 'Cannot open more than one file at once.')

def save_continue():
    '''Prompts user to save file, returns whether operation should proceed.'''
    if schedule.filename:
        answer = messagebox.askyesnocancel('', 'Save file before continuing?')
        if answer:
            save()
        elif answer == None:
            return False
    return True

def main(res_path):
    '''Called when package is run.'''
    global resource_path
    global schedule
    global t
    resource_path = res_path
    schedule = src.schedule.Schedule()
    t = tkinter.Tk()
    imgpath = os.path.join(resource_path, 'images')
    img = tkinter.PhotoImage(file=os.path.join(imgpath, 'icon.gif'))
    t.call('wm', 'iconphoto', t._w, img)
    t.protocol('WM_DELETE_WINDOW', close)
    t.title('Scheduler')
    t.resizable(0, 0)
    src.menusetup.setup(t)
    if platform.system() == 'Darwin' and sys.version_info[0] == 2:
        style = ttk.Style()
        style.configure('TNotebook.Tab', padding=(10, 8, 10, 0))
    notebook = ttk.Notebook(t)
    notebook.pack()
    bighex = tkinter.PhotoImage(file=os.path.join(imgpath, 'hex.gif'))
    heximg = bighex.subsample(2, 2)
    panels = {}
    for x in ('Courses', 'Instructors', 'Classes', 'Schedule'):
        panels[x] = src.panels.SearchPanel(bighex, x, notebook, 400)
    panels['Courses'].add_infobar('Taught By:')
    panels['Courses'].set_infobar_text('Taught By:', ['PROF_1', 'PROF_2'])
    panels['Courses'].add_search_bar('Courses', heximg)
    panels['Instructors'].add_infobar('Teaches:')
    panels['Instructors'].set_infobar_text('Teaches:', ['001', '002'])
    panels['Instructors'].add_search_bar('Instructors', heximg)
    panels['Classes'].add_search_bar('Courses', heximg)
    panels['Classes'].add_search_bar('Instructors', heximg)
    t.mainloop()
