class UndergroundSystem:

    def __init__(self):
        self.customerIn = {}
        self.timeRecord = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customerIn[id] = (stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.customerIn:
            startStation, startTime = self.customerIn[id]
            if (startStation, stationName) in self.timeRecord:
                self.timeRecord[(startStation, stationName)][0] += t - startTime
                self.timeRecord[(startStation, stationName)][1] += 1
            else:
                self.timeRecord[(startStation, stationName)] =  [t - startTime, 1]
            del self.customerIn[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        time, num = self.timeRecord.get((startStation, endStation), [0, 1])
        return time / num
            


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
