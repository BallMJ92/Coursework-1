class courseworkOne:

    #1.1 List containing the given set of elements
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
        if val1 in A and val2 in A and val3 in A:
            print("\nYes")
            print("List containing the given set of elements\n")
        else:
            print("\nNo")
            print("List not containing the given set of elements\n")

    #1.2 list containing the given set of elements in the given order
    def checkValsConsecutiveOrder(self):
        print("-----------------")
        print("1.2 List containing the given set of elements in the given order\n")

        # list
        A = []
        # values to test on list elements
        val1, val2, val3 = 1, 2, 3
        inOrder = 0

        #adding input to variable listLength
        listLength = int(input("Enter number of list elements: "))
        while listLength > 0:
            addElement = int(input("Enter element %d: " % (listLength)))
            A.append(addElement)
            listLength -= 1


        output = "\nNo \nList not containing the given set of elements in the given order\n"
        #checking each item in list and checking the order using the inOrder variable
        for i in A:
            if val1 == int(i):
                inOrder = 1
            if val2 == int(i) and inOrder == 1:
                    inOrder = 2
            if val3 == int(i) and inOrder == 2:
                    output = "\nYes \nList containing the given set of elements in the given order\n"

        print(output)

    #1.3 Lists containing the given set of elements consecutively and in the given order
    def checkValsOrder(self):
        print("-----------------")
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
            print("List containing the given set of elements consecutively and in the given order\n")
        else:
            print("\nNo")
            print("List not containing the given set of elements consecutively and in the given order\n")

    #2.1 Counting left and right brackets
    def countingBrackets(self):
        print("-----------------")
        print("Exercise 2 - String Processing")
        print("2.1 Counting left and right brackets\n")
        s = str(input("Enter string containing brackets: "))

        #counters for left and right brackets
        leftBrackets = 0
        rightBrackets = 0

        #checking each element in string and incrementing counters accourding to element
        for i in s:
            if i == ')':
                leftBrackets += 1
            elif i == '(':
                rightBrackets += 1

        print("\nThe string you entered contains %d right brackets and %d left brackets\n" % (rightBrackets, leftBrackets))

    #2.2 Testing whether the string is math-like
    def stringMathLike(self):
        print("-----------------")
        print("2.2 Testing whether the string is math-like\n")
        s = str(input("Enter string containing brackets: "))
        #dictionary holding left and right bracket
        bracketMap = {'(': ')'}
        #stack to add correct math-like brackets
        bracketList = []
        mathLike = ""
        yesOrNo = ""

        for brackets in s:
            #Checking equality in length of string. Making sure string length is even
            if len(s) % 2 == 0:
                # add math like bracket which corresponds to dictionary key to list
                if brackets in bracketMap:
                    bracketList.append((bracketMap[brackets]))
                    mathLike = "is math-like"
                    yesOrNo = "Yes"
                # checking if last item in bracketlist is not equal to value in bracketList or brackets
                elif not bracketList or brackets != bracketList.pop():
                    mathLike = "is not math-like"
                    yesOrNo = "No"
                    break
            else:
                mathLike = "is not math-like"
                yesOrNo = "No"
                break
        print("\n%s\nThe string %s %s" % (yesOrNo, s, mathLike))

    def main(self):
        self.checkVals()
        self.checkValsConsecutiveOrder()
        self.checkValsOrder()
        self.countingBrackets()
        self.stringMathLike()

if __name__ == "__main__":
    coursework = courseworkOne()
    coursework.main()
