class MyLinkedList:

    def __init__(self):
        self.linked = []

    def get(self, index: int) -> int:
        if index < len(self.linked) and index >= 0:
            return self.linked[index]
        return -1

    def addAtHead(self, val: int) -> None:
        self.linked.insert(0, val)

    def addAtTail(self, val: int) -> None:
        self.linked.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= len(self.linked) and index >= 0:
            self.linked.insert(index, val)

    def deleteAtIndex(self, index: int) -> None:
        if index < len(self.linked) and index >= 0:
            self.linked.pop(index)
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)