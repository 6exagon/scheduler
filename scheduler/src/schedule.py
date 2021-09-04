'''
Schedule class manages and serializes/deserializes schedule.
'''

def string(data):
    '''Returns string from data, with support for Python 2 and 3.'''
    try:
        return str(data, 'ascii')
    except TypeError:
        return str(data)

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
        self.filename = filename
        if filename:
            self.deserialize()
        else:
            self.profs = []
            self.courses = []
            self.descs = {}
            self.classes = []

    def serialize(self):
        '''Serializes schedule.'''
        fp = open(self.filename, 'wb')
        for x in self.courses:
            fp.write((x + '\n').encode('ascii'))
            fp.write((self.descs[x] + '\n').encode('ascii'))
        fp.write('\n'.encode('ascii'))
        for x in self.profs:
            fp.write((x + '\n').encode('ascii'))
        fp.write('\n'.encode('ascii'))
        try:
            for x in self.classes:
                fp.write(x.to_str())
        except TypeError:
            for x in self.classes:
                fp.write(x.to_bytes())
        fp.write('\x00\x00\x00'.encode('ascii'))

    def deserialize(self):
        '''Deserializes file data into schedule.'''
        self.profs = []
        self.courses = []
        self.descs = {}
        self.classes = []
        fp = open(self.filename, 'rb')
        while True:
            self.courses.append(string(fp.readline()[:-1]))
            if self.courses[-1] == '':
                del self.courses[-1]
                break
            self.descs[self.courses[-1]] = string(fp.readline()[:-1])
        while True:
            self.profs.append(string(fp.readline()[:-1]))
            if self.profs[-1] == '':
                del self.profs[-1]
                break
        while True:
            course_number = string(fp.read(3))
            if course_number == '\x00\x00\x00':
                break
            self.classes.append(Class(course_number, *fp.read(4)))

class Class:
    def __init__(self, course, prof_id, abstime, season_byte, days):
        '''Sets all fields to specified values.'''
        self.course = course
        try:
            self.prof_id = prof_id
            self.abstime = abstime
            self.season = chr(season_byte)
            self.days = days
        except TypeError:
            self.prof_id = ord(prof_id)
            self.abstime = ord(abstime)
            self.season = season_byte
            self.days = ord(days)

    def to_bytes(self):
        '''Returns binary representation of class (for Python 3).'''
        data = [self.prof_id, self.abstime, ord(self.season), self.days]
        return self.course.encode('ascii') + bytes(data)

    def to_str(self):
        '''Returns string representation of class (for Python 2).'''
        data = [self.prof_id, self.abstime, ord(self.season), self.days]
        return self.course + ''.join([chr(x) for x in data])
