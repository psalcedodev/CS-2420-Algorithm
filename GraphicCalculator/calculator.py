from graphics import *
from colors import *


class Stack:
    def __init__(self):
        self.mItems = []
        self.mLength = 0

    def top(self):
        if self.empty() == False:
            return self.mItems[self.mLength - 1]

    def push(self, item):
        self.mItems.append(item)
        self.mLength += 1

    def pop(self):
        if self.empty() == False:
            a = self.mItems.pop()
            self.mLength -= 1
            return a

    def empty(self):
        if len(self.mItems) == 0:
            return True
        else:
            return False


def printInstructions():
    # name = input('What is your name? ')
    # prMagenta('=======================================')
    # prYellow('Hi, %s!' % name)
    prYellow('I will help you get your graphic calculations!')
    prYellow('Your can use the following operatos:')
    prGreen('+ | Addition')
    prGreen('- | Substract')
    prGreen('* | Multiplication')
    prGreen('/ | Divide')


def main():
    printInstructions()

    userOperator = "(1+2*3)-(4/5*6-7)+8"
    prMagenta('=======================================')
    userOperator = InfixToPostfix(userOperator)
    print(userOperator)
    # win = GraphWin("Graphic Calculator", 600, 600)

    # Xlow = -100
    # Ylow = -100
    # Xhigh = +100
    # Yhigh = +100
    # win.setCoords(Xlow, Ylow, Xhigh, Yhigh)

    # Xpoints = []
    # Ypoints = []
    # x = Xlow
    # while x <= Xhigh:
    #     y = EvaluatePostfix(userOperator, x)

    #     Xpoints.append(x)
    #     Ypoints.append(y)
    #     x += .1

    # for i in range(len(Xpoints)-1):
    #     p1 = Point(Xpoints[i], Ypoints[i])
    #     p2 = Point(Xpoints[i+1], Ypoints[i+1])
    #     line = Line(p1, p2)
    #     line.draw(win)

    # lineX = Line(Point(Xlow, 0), Point(Xhigh, 0))
    # lineX.setOutline("red")
    # lineX.setWidth(3)
    # lineX.draw(win)
    # lineY = Line(Point(0, Ylow), Point(0, Yhigh))
    # lineY.setOutline("red")
    # lineY.setWidth(3)
    # lineY.draw(win)

    # win.getMouse()
    # win.close()


def InfixToPostfix(input):
    # * Stack initializer
    stack = Stack()
    postFix = ""
    # * Loops input
    for x in input:
        # * Check for the char to be a number or a var
        if x in "0123456789x":
            # * if x is a number or a variable, add it to the output
            postFix += x
        # * Checks if x starts with a parentheses
        elif x == "(":
            # * If yes, add it to the operators stack
            stack.push(x)
        # * Checks if x ends with a parentheses. if so, starts a while loop through the stack
        elif x == ")":
            while stack.empty() == False:
                # * Store the top char
                top = stack.top()
                # * Checks if char is an operator
                if top in "+-/*":
                    # * If true, pop the operator to the postfix
                    postFix += stack.pop()
                # * If top char is a left parentheses
                elif top == "(":
                    stack.pop()  # * then get rid of the top parenthesis
                    # * After getting rid of the top parentheses, break to leave the top
                    break

        elif x in "+-":
            top = stack.top()
            if stack.empty() or top == "(":
                stack.push(x)
            else:
                postFix += stack.pop()
                stack.push(x)
        elif x in "*/":
            top = stack.top()
            if stack.empty() or top not in "*/":
                stack.push(x)
            else:
                postFix += stack.pop()
                stack.push(x)
    while not stack.empty():
        postFix += stack.pop()
    return postFix


def EvaluatePostfix(input, value):
    stack = Stack()
    for x in input:
        if x in "x0123456789":
            if x == "x":
                stack.push(value)
            else:
                stack.push(float(x))
        elif x == "+":
            rhs = stack.pop()
            lhs = stack.pop()
            number = lhs + rhs
            stack.push(number)
        elif x == "-":
            rhs = stack.pop()
            lhs = stack.pop()
            number = lhs - rhs
            stack.push(number)
        elif x == "/":
            rhs = stack.pop()
            lhs = stack.pop()
            number = lhs / rhs
            stack.push(number)
        elif x == "*":
            rhs = stack.pop()
            lhs = stack.pop()
            number = lhs * rhs
            stack.push(number)
    return stack.top()


if __name__ == "__main__":
    main()
