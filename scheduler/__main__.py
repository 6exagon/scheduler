'''
Main package file.
'''

from inspect import getsourcefile
import os
import src.app

src.app.main(os.path.dirname(getsourcefile(lambda: 0)))
