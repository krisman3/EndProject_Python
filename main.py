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
            print("No available beds.")
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

    def release_patient(self, patient):
        if self.head is None:
            print("No patients to release.")
            return
        else:
            # Keep the released patient's name for the output:
            released_patient = self.head.data
            self.head = self.head.next
            self.size -= 1
            print(f"Patient {released_patient} released.")

    def is_empty(self):
        return self.head is None

