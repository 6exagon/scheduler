'''
Panel class and its subsidiaries manage display panels in the Notebook.
'''

try:
    import tkinter
    from tkinter import ttk
except ImportError:
    import Tkinter as tkinter
    import ttk

class SearchPanel:
    def __init__(self, icon, text, notebook, width):
        '''Sets up frame and inner components.'''
        self.frame = tkinter.Frame(notebook, borderwidth=0, bg='#ddd')
        self.frame.pack(fill='both', expand=True)
        notebook.add(self.frame, text=text)
        self.width = width
        self.iconlabel = tkinter.Label(self.frame, image=icon, borderwidth=0)
        self.iconlabel.grid(row=0, column=0, columnspan=2)
        self.rows = 1
        self.sbars = {}
        self.ibars = {}

    def add_infobar(self, title):
        '''Adds InfoBar to panel.'''
        self.ibars[title] = InfoBar(self.frame, title, self.rows)
        self.rows += 2
    
    def add_search_bar(self, name, icon):
        '''Adds SearchBar to panel.'''
        self.sbars[name] = SearchBar(self.frame, icon, self.rows)
        self.rows += 1

    def set_infobar_text(self, bar, infolist):
        '''Sets the text of a named InfoBar.'''
        self.ibars[bar].set_text(infolist)
        

class InfoBar:
    def __init__(self, frame, title, row, editable=False):
        '''Creates InfoBar and properly displays it.'''
        self.label = tkinter.Label(frame, font=('Times', 20), bg='#ddd')
        self.label.config(text=title)
        self.label.grid(row=row, column=0, columnspan=2)
        if editable:
            self.bar = tkinter.Entry(frame, font=('Helvetica', 24))
        else:
            self.bar = tkinter.Label(frame, font=('Helvetica', 24), bg='#ddd')
        self.bar.grid(row=row + 1, column=0, columnspan=2)

    def set_text(self, infolist):
        '''Sets the text within an InfoBar field.'''
        self.bar.config(text=', '.join(infolist))

class SearchBar:
    def __init__(self, frame, icon, row):
        '''Creates SearchBar and properly displays it.'''
        self.label = tkinter.Label(frame, image=icon, borderwidth=0)
        self.label.grid(row=row, column=0)
        self.bar = tkinter.Entry(frame, font=('Courier', 40), width=20)
        self.bar.grid(row=row, column=1)
