class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = None 


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
    for va in str(val3):
        append(int(va))


def getLinkedListValues(linkedList):
    value = ""
    
    currentValue = linkedList

    while currentValue:
        value += str(currentValue.val)
        currentValue = currentValue.next
        
    # Return value as integer after reversing
    return int(value[::-1])


# This function is defined in Linked List
# class appends a new node at the end.
# This method is defined inside LinkedList
# class shown above
def append(new_data):
   global head

   # 1. Create a new node
   # 2. Put in the data
   # 3. Set next as None
   new_node = ListNode(new_data)

   # 4. If the Linked List is empty, then
   #    make the new node as head
   if head is None:
       head = new_node
       return

   # 5. Else traverse till the last node
   last = head
   while (last.next):
       last = last.next

   # 6. Change the next of last node
   last.next = new_node


def printLinkedList(linkedList):
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

e111 = ListNode(8)
e222 = ListNode(0)
e333 = ListNode(7)

e111.next = e222
e222.next = e333
v3 = e111

print("Passed!" if addTwoNumbers(l1=v1, l2=v2) == v3 else "Failed!")