#2. stack implementation with size limit
import sys
class Stack:
    def __init__(self,stackSize):
        self.stackList = []    #stack created
        self.stackSize = stackSize

    def isFull(self):
        if len(self.stackList) == self.stackSize:
            return True
        else:
            return False

    def push(self,value):
        if self.isFull():
            print("stack is full")
        else:
            self.stackList.append(value)

    def displayStack(self):
        print(" --------------------------------- ")
        print(self.stackList)
        print(" --------------------------------- ")

    def isEmpty(self):
        if self.stackList == []:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.stackList.pop()
        
    def deleteStack(self):
        self.stackList = None
        return "stack is deleted"
    
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            return self.stackList[-1]

size = int(input("Enter the size of stack : "))
stackObj = Stack(size)                           #stack object is created

while True :
    print(" ======================================= ")
    print("1. Push Element in stack ")
    print("2. Display stack element ")
    print("3. check whether stack is empty ")
    print("4. Pop the element from stack")
    print("5. delete element")
    print("6. peek operation")
    print("7. exit")

    choice = int(input("Enter your choice : "))
    if choice == 1:
        val = int(input("ENter the value for stack : "))
        stackObj.push(val)

    elif choice == 2:
        stackObj.displayStack()

    elif choice == 3:
        print(stackObj.isEmpty())

    elif choice == 4:
        print("popped element : ",stackObj.pop())

    elif choice == 5:
        print(stackObj.deleteStack())

    elif choice == 6:
        print(stackObj.peek())

    elif choice == 7:
        sys.exit()