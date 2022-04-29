class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: "Optional[ListNode]", l2: "Optional[ListNode]") -> "Optional[ListNode]":
    val1 = 0
    val2 = 0

    val1 = getLinkedListValues(l1)
    val2 = getLinkedListValues(l2)

    val3 = val1 + val2

    print(getLinkedListValues(l1))
    print(getLinkedListValues(l2))

    # Convert value to string, reverse, then turn back to integer
    # print(int(str(val3)[::-1]))

    addToLinkedList(str(val3))


def getLinkedListValues(linkedList):
    value = ""
    
    currentValue = linkedList

    while currentValue:
        value += str(currentValue.val)
        currentValue = currentValue.next
        
    # Return value as integer after reversing
    return int(value[::-1])


def addToLinkedList(val):
    output = ListNode(val[0])

    for v in  val:
        output.next = ListNode(int(v))

    listprint(output)
    return output


def listprint(linkedList):
    theLst = linkedList

    while theLst is not None:
        print(theLst.val)
        theLst = theLst.next


# Test Cases
e1 = ListNode(2)
e2 = ListNode(4)
e3 = ListNode(3)

e1.next = e2
e2.next = e3
v1 = e1

e11 = ListNode(5)
e22 = ListNode(6)
e33 = ListNode(4)

e11.next = e22
e22.next = e33
v2 = e11

print("Passed!" if addTwoNumbers(l1=v1, l2=v2) == [7,0,8] else "Failed!")
# print("Passed!" if addTwoNumbers(nums=[-1,-2,-3,-4,-5], target=-8) == [2,4] else "Failed!")
# print("Passed!" if addTwoNumbers(nums=[-3,4,3,90], target=0) == [0,2] else "Failed!")