class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete(self, node):
        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
        else:
            prev_node = node.prev
            next_node = node.next
            if prev_node:
                prev_node.next = next_node
            if next_node:
                next_node.prev = prev_node

    def print_lines(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append_document(self, linked_list):
        new_node = Node(linked_list)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete_document(self, node):
        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
        else:
            prev_node = node.prev
            next_node = node.next
            if prev_node:
                prev_node.next = next_node
            if next_node:
                next_node.prev = prev_node

    def print_documents(self):
        current = self.head
        while current:
            print("Document:")
            current.data.print_lines()
            current = current.next


class Notepad:
    def __init__(self):
        self.documents = DoubleLinkedList()
        self.current_document = None
        self.current_line = None

    def create_document(self):
        linked_list = LinkedList()
        self.documents.append_document(linked_list)
        self.current_document = self.documents.head
        self.current_line = None

    def open_document(self, document_index):
        current = self.documents.head
        count = 0
        while current and count < document_index:
            current = current.next
            count += 1
        if current:
            self.current_document = current
            self.current_line = None
        else:
            print("Document not found.")

    def save_document(self, document_index):
        current = self.documents.head
        count = 0
        while current and count < document_index:
            current = current.next
            count += 1
        if current:
            # Save document logic can be implemented here
            print("Document saved.")
        else:
            print("Document not found.")

    def insert_line(self, text):
        if self.current_document:
            if not self.current_line:
                self.current_document.data.append(text)
            else:
                new_node = Node(text)
                current = self.current_line
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
        else:
            print("No document open.")

    def delete_line(self):
        if self.current_line:
            if self.current_line == self.current_document.data.head:
                self.current_document.data.head = self.current_line.next
                if self.current_line.next:
                    self.current_line.next.prev = None
            else:
                self.current_document.data.delete(self.current_line)
            self.current_line = None
        else:
            print("No line to delete.")

    def move_up(self):
        if self.current_line and self.current_line.prev:
            self.current_line = self.current_line.prev
        else:
            print("Already at the beginning of the document.")

    def move_down(self):
        if self.current_line and self.current_line.next:
            self.current_line = self.current_line.next
        else:
            print("Already at the end of the document.")

    def print_current_document(self):
        if self.current_document:
            self.current_document.data.print_lines()
        else:
            print("No document open.")

    def print_all_documents(self):
        self.documents.print_documents()

# Example usage:
notepad = Notepad()

# Create a new document
notepad.create_document()

# Insert lines into the current document
notepad.insert_line("Line 1")
notepad.insert_line("Line 2")
notepad.insert_line("Line 3")

# Print current document
print("Current Document:")
notepad.print_current_document()

# Move up and down in the document
notepad.move_up()
print("After moving up:")
notepad.print_current_document()

notepad.move_down()
print("After moving down:")
notepad.print_current_document()

# Open a new document
notepad.create_document()
notepad.insert_line("New Document Line 1")
notepad.insert_line("New Document Line 2")

# Print all documents
print("All Documents:")
notepad.print_all_documents()

# Save a document
notepad.save_document(1)
