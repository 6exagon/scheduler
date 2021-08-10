'''
Class class manages class struct.
'''

class Class:
    def __init__(self, course, prof_id, abstime, season_byte, days):
        '''Sets all fields to specified values.'''
        self.course = course
        self.prof_id = prof_id
        self.abstime = abstime
        self.season = chr(season_byte)
        self.days = days

    def to_bytes(self):
        '''Returns binary representation of class.'''
        data = bytes([self.prof_id, self.abstime, ord(self.season), self.days])
        return self.course.encode('ascii') + data
