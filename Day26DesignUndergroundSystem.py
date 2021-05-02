#Day 26 of 365 days of code
#Link for leetcode:https://leetcode.com/problems/design-underground-system/

#An underground railway system is keeping track of customer travel times between different stations. 
#They are using this data to calculate the average time it takes to travel from one station to another.

#Implement the UndergroundSystem class:
#void checkIn(int id, string stationName, int t)
#A customer with a card ID equal to id, checks in at the station stationName at time t.
#A customer can only be checked into one place at a time.
#void checkOut(int id, string stationName, int t)
#A customer with a card ID equal to id, checks out from the station stationName at time t.
#double getAverageTime(string startStation, string endStation)
#Returns the average time it takes to travel from startStation to endStation.
#The average time is computed from all the previous traveling times from startStation to endStation that happened directly, 
#meaning a check in at startStation followed by a check out from endStation.
#The time it takes to travel from startStation to endStation may be different from the time it takes to travel from endStation 
#to startStation.
#There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.
#You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks in at time t1 then checks out 
#at time t2, then t1 < t2. All events happen in chronological order.

class UndergroundSystem:
    class Station:
        def __init__(self, stationName, startTime):
            self.stationName = stationName;
            self.startTime = startTime
            
    class StationTotals:
        def __init__(self):
            self.totalJourneyTime = 0;
            self.totalPassengers = 0;

    def __init__(self):
        self.checkInTime = {}
        self.runningTotals = {}

    def checkIn(self, id, stationName, t):
        self.checkInTime[id] = self.Station(stationName, t); #Id can't check in again, until it has checked out, so this 
                                        #will only get over written, once we have already updated totals in check out
        

    def checkOut(self, id, stationName, t):
        startingStation = self.checkInTime[id].stationName;
        startTime = self.checkInTime[id].startTime;
        timeTaken = t - startTime;
        if not startingStation in self.runningTotals:
            self.runningTotals[startingStation] = {};
        if not stationName in self.runningTotals[startingStation]:
            self.runningTotals[startingStation][stationName] = self.StationTotals();
        
        self.runningTotals[startingStation][stationName].totalJourneyTime += timeTaken;
        self.runningTotals[startingStation][stationName].totalPassengers +=1;

    def getAverageTime(self, startStation, endStation):
        totals = self.runningTotals[startStation][endStation];
        return totals.totalJourneyTime / totals.totalPassengers;

