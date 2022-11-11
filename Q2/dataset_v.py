n = int(input())
arr = []
for i in range(n):
    curr = input()
    a = curr.split()
    arr.append(a)



def check_validity(arr):
    errorCodes, allValid = [], True
    
    for i in range(len(arr)):
        if arr[i][1] == "true":
            continue
        if arr[i][1] == "false":
            allValid = False
            errorCodes.append(arr[i][2])

    if allValid == True:
        print("Yes")
    elif allValid == False:
        print("No")

    for ec in errorCodes:
        print(ec, end=" ")

check_validity(arr)

