class Time:
    def timeDiff(self, strArr):
        if not strArr:
            return 0
        minuteList = list(map(self.timeConvert, strArr))
        minuteList.sort()
        minDiff = float('inf')

        for i in range(1, len(minuteList)):
            timeDiff = minuteList[i] - minuteList[i - 1]
            minDiff = min(minDiff, timeDiff)

        diffOfFirstAndLast = 24 * 60 - (minuteList[-1] - minuteList[0])
        minDiff = min(minDiff, diffOfFirstAndLast)
        return minDiff

    def timeConvert(self, time):
        length = len(time)
        timeList = time[:length - 2].split(':')

        if time[-2] + time[-1] == 'pm' and int(timeList[0]) != 12:
            return (int(timeList[0]) + 12) * 60 + int(timeList[1])
        elif time[-2] + time[-1] == 'am' and int(timeList[0]) == 12:
            return int(timeList[1])
        else:
            return int(timeList[0]) * 60 + int(timeList[1])

        # if time[-2] + time[-1] == 'pm':
        #     if int(timeList[0]) == 12:
        #         return int(timeList[0]) * 60 + int(timeList[1])
        #     return (int(timeList[0]) + 12) * 60 + int(timeList[1])
        # else:
        #     if int(timeList[0]) == 12:
        #         return int(timeList[1])
        #     else:
        #         return int(timeList[0]) * 60 + int(timeList[1])



if __name__ == '__main__':
    list1 = ['1:10pm', '4:40am', '5:00pm']
    list2 = ['10:00am', '11:45pm', '5:00am', '12:01am']
    list3 = ['2:10pm', '1:30pm', '10:30am', '4:42pm']
    list4 = ['2:10pm', '11:48am', '10:30am', '12:01pm']
    t = Time()
    print(t.timeDiff(list1))
    print(t.timeDiff(list2))
    print(t.timeDiff(list3))
    print(t.timeDiff(list4))
