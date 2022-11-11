def toNum(str):
    if len(str) == 1:
        if str == 'S':
            return 0
        if str == 'M':
            return 1
        if str == 'L':
            return 2
    if len(str) > 1 and str[-1] == 'S':
        curr = 0
        for char in str:
            if char == 'X':
                curr -= 1
        return curr
    elif len(str) > 1 and str[-1] == 'L':
        curr = 2
        for char in str:
            if char == 'X':
                curr += 1
        return curr


def algo1(shopNum, shopList, wantNum, wantList):
    # size = []
    d = {}
    if wantNum > shopNum:
        print("No") 
    for x in shopList:
        val = toNum(x)
        if val not in d.keys():
            d[val] = 1
        else:
            d[val] += 1

    # print(d)
    # flag = 0
    count = 0
    for y in wantList:
        # print(y)
        # have = False
        val = toNum(y)
        # print(val)
        for i in range(val, 1004):
            # print(val, i)
            if i in d.keys() and d[i] >= 1:
                # print('HAVE')
                count += 1
                # have = True
                d[i] -= 1
                # print(i)
                # print("No")
                break
    # print(count)
    
            
    if count == len(wantList):
        print("Yes")
    else:
        print("No")

    # return

        
shopNum = int(input())
shopList = input().split()
while len(shopList) != shopNum:
    shopList = input().split()

# print(shopList)

wantNum = int(input()) 
wantList = input().split()
while len(wantList) != wantNum:
    wantList = input().split()
# print(wantList)


algo1(shopNum, shopList, wantNum, wantList)
                


        
        

        
    