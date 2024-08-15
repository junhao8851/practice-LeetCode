class MyLinkedList:

    def __init__(self):

        self.head = ListNode()

        self.length = 0


    def get(self, index: int) -> int:

        if index < 0 or index >= self.length:

            return -1

        res = self.head.next

        while index:

            res = res.next

            index -= 1

        return res.val


    def addAtHead(self, val: int) -> None:

        self.head.next = ListNode(val, self.head.next)

        self.length += 1


    def addAtTail(self, val: int) -> None:

        res = self.head

        while res.next:

            res = res.next

        res.next = ListNode(val, None)

        self.length += 1


    def addAtIndex(self, index: int, val: int) -> None:

        if index > self.length:

            return

        if index <= 0:

            self.addAtHead(val)

        else:

            tag = self.head

            while index:

                tag = tag.next

                index -= 1

            tag.next = ListNode(val, tag.next)

            self.length += 1


    def deleteAtIndex(self, index: int) -> None:

        if index < 0 or index >= self.length:

            return

        tag = self.head

        while index:

            tag = tag.next

            index -= 1

        tag.next = tag.next.next

        self.length -= 1