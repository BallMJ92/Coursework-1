class courseworkOne:

    def checkVals(self):
        print("Exercise 1 - List Processing")
        print("1.1 List containing the given set of elements\n")

        # list
        A = []
        # values to test on list elements
        val1, val2, val3 = 1, 2, 3

        # adding input to variable listLength
        listLength = int(input("Enter number of list elements: "))
        while listLength > 0:
            addElement = int(input("Enter element %d: " % (listLength)))
            A.append(addElement)
            listLength -= 1

        #checking if values appear in list A
        if (val1 and val2 and val3) in A:
            print("\nYes")
            print("List containing the given set of elements\n")
        else:
            print("\nNo")
            print("List not containing the given set of elements\n")

    def checkValsConsecutiveOrder(self):
        print("1.2 List containing the given set of elements in the given order\n")

        # list
        A = []
        # values to test on list elements
        val1, val2, val3 = 1, 2, 3

        #adding input to variable listLength
        listLength = int(input("Enter number of list elements: "))
        while listLength > 0:
            addElement = int(input("Enter element %d: " % (listLength)))
            A.append(addElement)
            listLength -= 1

        #checking if values appear as individual elements in list A
        output = ""
        for i in A:
            x = i
            if (str(val1 and val2 and val3)) in str(x):
                output = "\nYes \nList containing the given set of elements in the given order"
            else:
                output = "\nNo \nList not containing the given set of elements in the given order"

        print(output)

    def checkValsOrder(self):
        print("1.3 List containing the given set of elements consecutively and in the given order\n")

        # list
        A = []
        # values to test on list elements
        val1, val2, val3 = 1, 2, 3

        # adding input to variable listLength
        listLength = int(input("Enter number of list elements: "))
        while listLength > 0:
            addElement = int(input("Enter element %d: " % (listLength)))
            A.append(addElement)
            listLength -= 1

        #iterating over list A to check if the value set appears in order within list
        if any([val1, val2, val3] == A[i:i + 3] for i in range(len(A) - 1)):
            print("\nYes")
            print("List containing the given set of elements consecutively and in the given order")
        else:
            print("\nNo")
            print("List not containing the given set of elements consecutively and in the given order")

    def countingBrackets(self):
        print("2.1 Counting left and right brackets\n")
        bracketCounting = str(input("Enter string containing brackets: "))

        #counters for left and right brackets
        leftBrackets = 0
        rightBrackets = 0

        #checking each element in string and incrementing counters accourding to element
        for i in bracketCounting:
            if i == ')':
                leftBrackets += 1
            elif i == '(':
                rightBrackets += 1
            else:
                print("No brackets entered")

        print("\nThe string you entered contains %d right brackets and %d left brackets" % (rightBrackets, leftBrackets))

    def stringMathLike(self):
        print("2.2 Testing whether the string is math-like\n")
        bracketCount = str(input("Enter string containing brackets: "))
        #dictionary mapping left bracket with right bracket
        bracketMap = {'(': ')'}
        #stack to add correct math-like brackets
        stack = []
        mathLike = ""

        for brackets in bracketCount:
            if brackets in bracketMap:
                stack.append((bracketMap[brackets]))
                mathLike = "is math-like"
            elif not stack or brackets != stack.pop():
                mathLike = "is not math-like"
                break

        print("\nThe string %s %s" % (bracketCount, mathLike))

    def main(self):
        #self.checkVals()
        #self.checkValsConsecutiveOrder()
        #self.checkValsOrder()
        #self.countingBrackets()
        self.stringMathLike()

if __name__ == "__main__":
    coursework = courseworkOne()
    coursework.main()
