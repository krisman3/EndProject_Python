### Task 4 ###

class Patient:
    def __init__(self, name):
        self.name = name
# Operating room
class OperatingRoom:

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None
        self.size = 0

    def admit_patient(self, patient):
        if self.size >= self.capacity:
            print("The operating room is currently full!")
            return

        new_node = self.Node(patient)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1
        print(f"Patient {patient.name} admitted.")

    def is_empty(self):
        if self is None and self.next is None:
            return True
        return False