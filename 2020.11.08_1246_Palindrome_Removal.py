class Solution(object):
    def mctFromLeafValues(self, arr):
        res = 0
        for i in range(1,len(arr)):
            start = i-1
            temp = arr[start]
            while start>=0 and arr[start]<arr[i]:
                temp = max(temp,arr[start])
                start = start -1
            if start ==i-1 or start<0:
                res+=arr[i]*temp
            else:
                res+= arr[i]*temp+arr[start]*(arr[i]-temp)
        return res