'''
Main entry point of program, handles code at top level.
'''

import os
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter
import src.schedule

def main(resource_path):
    '''Called when package is run.'''
    t = tkinter.Tk()
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
