class Currency:
    def isCurrency(self, str):
        validSymbol = {'$', '€', '¥'}
        if not str:
            return False
        length = len(str)
        if str[0] not in {'-', '(', '$', '€', '¥'}:
            return False

        if str[0] == '(':
            if str[1] not in validSymbol or \
                    not str[2].isdigit() or str[-1] != ')':
                return False
            return self.isValidCents(str[1: length - 1]) \
                   and self.isValidThousSep(str[2:length - 1])

        if str[0] == '-':
            if str[1] not in validSymbol:
                return False
            return self.isValidCents(str[1:]) \
                   and self.isValidThousSep(str[2:])

        if str[0] in validSymbol:
            if not str[1].isdigit() or str[1] == '0':
                return False
            return self.isValidCents(str) \
                   and self.isValidThousSep(str[1:])

    def isValidCents(self, str):
        strSet = set(str)
        if '¥' in strSet and '.' not in strSet:
            return True
        elif '$' in strSet or '€' in strSet:
            if '.' not in set(str) or str[-3] == '.':
                return True
        return False

    def isValidThousSep(self, str):
        n = len(str)
        strSet = set(str)
        if ',' not in strSet:
            return True
        if '.' in strSet:
            return self.isValidThousSep(str[:n-3])
        for i in range(len(str)):
            if (str[i] == ',' and (i - n) % 4 != 0) \
                or (i - n) % 4 == 0 and str[i] != ',':
                return False
        return True


if __name__ == '__main__':
    c = Currency()
    strList = ['¥450', '-€23', '(¥2400)', '€0.25', 'cat', '£25', \
               '$45,0', '(€350', '(-$3.50)', '¥120.00', '$-50', \
               '$4,500.00', '($)', '$01', '$01.25']
    for elem in strList:
        print(c.isCurrency(elem))
