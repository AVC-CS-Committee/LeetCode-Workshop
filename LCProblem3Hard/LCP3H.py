from collections import deque

s = "([{}])" #this is the example string

def LCProblem2Hard(): #this function prints the variables (do not remove this function)
    
    stack = deque()
            
    for i in s:
        if i == '(' or i == '[' or i == '{': #checks to see if the character is an opening bracket
            stack.append(i)
        else:
            if not stack: #instantly returns false if the stack is empty
                return False
            #these if statemetns check to see if the closing bracket matches the opening bracket
            if i == ')' and stack[-1] == '(':
                stack.pop()
            elif i == ']' and stack[-1] == '[':
                stack.pop()
            elif i == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
    return True

    
print(LCProblem2Hard()) #this line calls the function to print the variables (do not remove this line)