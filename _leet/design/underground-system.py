"""
https://leetcode.com/problems/design-underground-system/

underground
railway station
car parking
toll both


"""
class UndergroundSystem:

    def __init__(self):
        # {id:[checkInStation, checkInTime],  }
        self.checkindata={}
        # [(checkInStation, checkOutStation): journeyTime, Count,  ]
        self.journeydata=collections.defaultdict(lambda: [0,0])
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkindata[id]=[stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # instead of getting value like self.checkindata[id]
        # just pop checkin data, this is no longer useful and keep our performance intact
        checkInStation, checkInTime = self.checkindata.pop(id)
        self.journeydata[(checkInStation, stationName)][0]+=t-checkInTime
        self.journeydata[(checkInStation, stationName)][1]+=1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, trips = self.journeydata[(startStation, endStation)]
        return total/trips


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)