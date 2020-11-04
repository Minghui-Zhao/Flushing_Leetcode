import collections

class UndergroundSystem:
    def __init__(self):
        self.enter = collections.defaultdict(list)
        self.exit = collections.defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # self.stationAndTime[start] = [stationName, t]
        # self.info[id] = self.stationAndTime
        self.enter[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # self.info[id][end] = [stationName, t]
        enterStation, enterTime = self.enter[id]
        self.exit[(enterStation, stationName)].append(t - enterTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # sumTime = 0
        # totalCount = 0
        # for id, information in self.info.items():
        #     if information[start][0] == startStation and information[end][0] == endStation:
        #         sumTime += information[end][1] - information[start][1]
        #         totalCount += 1
        # return sumTime // totalCount if totalCount > 0 else None

        return float(sum(self.exit[(startStation, endStation)])) / len(self.exit[(startStation, endStation)])
