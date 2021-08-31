'''
Class class manages class struct.
'''

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
