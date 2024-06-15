class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
    
    def delete_last(self):
        if self.tail:
            if self.tail.prev:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.head = None
                self.tail = None
            return True
        return False

class UndoableNotepad:
    def __init__(self):
        self.content = DoublyLinkedList()
        self.undo_stack = []

    def add_text(self, text):
        self.content.append(text)
        self.undo_stack.append("add")

    def delete_last_character(self):
        if self.content.delete_last():
            self.undo_stack.append("delete")
    
    def undo(self):
        if self.undo_stack:
            action = self.undo_stack.pop()
            if action == "add":
                self.content.delete_last()
            elif action == "delete":
                # Revert the last delete action (not implemented in this simplified example)

# Example usage:
notepad = UndoableNotepad()
notepad.add_text("Hello")
notepad.add_text("World")
print("Current Content:", [node.data for node in notepad.content])
notepad.delete_last_character()
print("Content after delete:", [node.data for node in notepad.content])
notepad.undo()
print("Content after undo:", [node.data for node in notepad.content])
