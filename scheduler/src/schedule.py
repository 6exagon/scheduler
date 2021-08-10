'''
Schedule class manages and serializes/deserializes schedule.
'''

import src.sclass

def abstime(time_string):
    '''Returns time in minutes since 8:00 divided by 10.'''
    timelist = [int(x) for x in time_string.split(':')]
    return (timelist[0] - 8) % 12 * 6 + timelist[1] // 10

def stringtime(abs_time):
    '''Reformats time into string.'''
    hours = str((abs_time // 6 + 8) % 12)
    if hours == '0':
        hours = '12'
    minutes = str(abs_time % 6 * 10)
    if minutes == '0':
        minutes = '00'
    return hours + ':' + minutes

class Schedule:
    def __init__(self, filename=None):
        '''Prepares lists, retrieves data from file if applicable.'''
        if filename:
            self.deserialize(filename)
        else:
            self.profs = []
            self.courses = []
            self.descs = {}
            self.classes = []

    def serialize(self, filename):
        '''Serializes schedule.'''
        fp = open(filename, 'wb')
        for x in self.courses:
            fp.write((x + '\n').encode('ascii'))
            fp.write((self.descs[x] + '\n').encode('ascii'))
        fp.write('\n'.encode('ascii'))
        for x in self.profs:
            fp.write((x + '\n').encode('ascii'))
        fp.write('\n'.encode('ascii'))
        for x in self.classes:
            fp.write(x.to_bytes())
        fp.write('\x00\x00\x00'.encode('ascii'))

    def deserialize(self, filename):
        '''Deserializes file data into schedule.'''
        self.profs = []
        self.courses = []
        self.descs = {}
        self.classes = []
        fp = open(filename, 'rb')
        while True:
            self.courses.append(str(fp.readline()[:-1], 'ascii'))
            if self.courses[-1] == '':
                del self.courses[-1]
                break
            self.descs[self.courses[-1]] = str(fp.readline()[:-1], 'ascii')
        while True:
            self.profs.append(str(fp.readline()[:-1], 'ascii'))
            if self.profs[-1] == '':
                del self.profs[-1]
                break
        while True:
            course_number = str(fp.read(3), 'ascii')
            if course_number == '\x00\x00\x00':
                break
            self.classes.append(src.sclass.Class(course_number, *fp.read(4)))
