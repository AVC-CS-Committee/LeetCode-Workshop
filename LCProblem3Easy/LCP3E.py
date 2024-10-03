def LCProblem2Easy(): #this function prints the variables (do not remove this function)
    listLength = input("Enter list number: ")
    numList = []
    for i in range(int(listLength)):
        num = int(input("Enter a number: "))
        numList.append(num)

    evenCount = 0
    for i in numList:
        if i % 2 == 0:
            evenCount += 1
    print(evenCount)

    
print(LCProblem2Easy()) #this line calls the function to print the variables (do not remove this line)