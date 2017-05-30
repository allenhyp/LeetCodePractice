def longestPalindrome(s):
    if len(s) <= 1:
        return s
    stack = [s[0]]
    top = 0
    tmpLen = 0
    longestLen = 0
    i = 0
    j = 0
    ls = len(s)
    working = False
    tail = 0
    head = ls - 1

    while True:
        if i + 1 < ls:
            i += 1
            j += 2
        else:
            break
        print "interate to s[{}]: {}".format(i, s[i])
        print stack
        if not working:
            if s[i] == stack[top]:
                print "even: {},{}".format(i, top)
                j = 0
                tmpLen = 2
                working = True

            elif s[i] == stack[top - 1]:
                print "odd: {},{}".format(i, top)
                j = 1
                tmpLen = 3
                working = True

        else:
            print "matching: {},{}".format(i, top - j)
            if top - j >= 0:
                if s[i] == stack[top - j]:
                    tmpLen += 2
                else:
                    working = False
            else:
                working = False
            print "now tmpLen = {}".format(tmpLen)

        if longestLen < tmpLen:
            tail = i - tmpLen + 1
            head = i
            longestLen = tmpLen
            print "tail = {}".format(tail)
            print "head = {}".format(head)

        stack.append(s[i])
        top += 1

    if longestLen > 1:
        print "===========\nresult: "
        return s[tail:head + 1]


inputStr = raw_input("Input: ")
print longestPalindrome(inputStr)
