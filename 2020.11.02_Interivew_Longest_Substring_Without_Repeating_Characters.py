
def longestSubstringLength(s):
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1

    slow = 0
    count = {}
    maxLen = 0
    for fast in range(len(s)):
        curChar = s[fast]
        if curChar not in count:
            count[curChar] = 1
        else:
            count[curChar] = count.get(curChar) + 1
            while count[curChar] > 1:
                count[s[slow]] -= 1
                if count[s[slow]] == 0:
                    del count[s[slow]]
                slow += 1
            # print(count)
        if (fast - slow + 1) > maxLen:
            maxLen = fast - slow + 1
            # print(maxLen)
    return maxLen

if __name__ == '__main__':
    # print(longestSubstringLength('abac'))
    print(longestSubstringLength('abcabcabchgik'))