#!/usr/bin/env python3

def print_fibonacci(length):
    fibList = []
    if length > 0:
        for lenSpot in range(length):
            if lenSpot == 0 :
                fibList.append(0)
            elif lenSpot == 1:
                fibList.append(1)
            else:
                # print ("current list ", fibList)
                # print("lenSpot ", lenSpot)
                # print("fibList[1] = ", fibList[lenSpot-1])
                if len(fibList) >= 2:
                    nextValue = fibList[lenSpot-1] + fibList[lenSpot-2]
                    fibList.append(nextValue)
    
    print(fibList)

print_fibonacci(3)