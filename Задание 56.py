from datetime import datetime

class Period:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def getSeconds(self):
        diff = self.end - self.start
        return diff.total_seconds()

    def getMinutes(self):
        diff = self.end - self.start
        return diff.total_seconds() / 60

    def getHours(self):
        diff = self.end - self.start
        return diff.total_seconds() / 3600

    def getDays(self):
        diff = self.end - self.start
        return diff.days

start = datetime(2023, 2, 5, 1, 12, 1)
end = datetime(2023, 1, 6, 1, 1, 31)
period = Period(start, end)

print(period.getSeconds())
print(period.getMinutes())
print(period.getHours())
print(period.getDays())