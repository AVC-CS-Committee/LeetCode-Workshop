def LCProblem2Easy(): #this function prints the variables (do not remove this function)
    listLength = input('Enter the length of list: ')
    numList = []
    for i in range(int(listLength)):
        num = int(input('Enter a number: '))
        numList.append(num)

    addSum = 0
    for i in numList:
        addSum += i
    
    return addSum

    
print(LCProblem2Easy()) #this line calls the function to print the variables (do not remove this line)