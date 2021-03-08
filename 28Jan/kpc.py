def getStr(a):
    numStr = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    return numStr[a]


def printKPC(q, a):
    if len(q) == 0:
        print(a)
        return
    
    ch = q[0]
    string = getStr(ch)
    rest = q[1: ]
    for i in string:
        printKPC(rest, a + i)
    

printKPC("32", "")