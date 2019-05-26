"""
Class for storing time. Time is reported on a military (24 hour) clock. We
use a list to store hours minutes and seconds as list[0], list[1] and list[2]
explicitly
"""


class Time(object):
    def __init__(self, hr=0, minute=0, sec=0):
        self.time = [hr, minute, sec]
        
    def convert(self):
        pass
        
    def __str__(self):
        return "{:02d}:{:02d}:{:02d}".format(self.time[0], self.time[1], self.time[2])
    
    def __add__(self, other):
        new_hrs = self.time[0] + other.time[0]
        new_mins = self.time[1] + other.time[1]
        new_secs = self.time[2] + other.time[2]
        
        add_minutes = new_secs // 60
        new_secs = new_secs % 60
        
        new_mins += add_minutes
        add_hours = new_mins // 60
        new_mins = new_mins % 60
        
        new_hrs += add_hours
        new_hrs = new_hrs % 24
        
        return Time(new_hrs, new_mins, new_secs)
    
    def __sub__(self, other):
        seconds = self.time[2] + 60 * self.time[1] + 60 * 60 * self.time[0]
        other_seconds = other.time[2] + 60 * other.time[1] + 60 * 60 * other.time[0]
        new_seconds = max(0, seconds-other_seconds)
        
        new_hrs = new_seconds // 3600
        new_seconds = new_seconds % 3600
        new_mins = new_seconds // 60
        new_seconds = new_seconds % 60
        
        return Time(new_hrs, new_mins, new_seconds)


if __name__ == '__main__':
    t1 = Time()
    print(str(t1))
    t2 = Time(10, 29, 37)
    print(str(t2))
    t3 = Time(23, 59, 59)
    print(str(t3))
    
    print("{} + {} = {}".format(t3, t3, t3 + t3))
    print("{} - {} = {}".format(t1, t2, t1 - t2))
    print("{} - {} = {}".format(t2, t1, t2 - t1))
    print("{} - {} = {}".format(t2, t3, t2 - t3))
    print("{} - {} = {}".format(t3, t2, t3 - t2))
