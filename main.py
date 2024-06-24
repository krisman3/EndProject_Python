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
        self.capacity = int(capacity)
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

    def current_patients(self):
        patients = []
        current = self.head
        while current is not None:
            patients.append(current.data.name)
            current = current.next
        return patients

    def is_empty(self):
        return self.head is None

    def is_full(self):
        patients = []
        current = self.head
        while current is not None:
            patients.append(current.data.name)
            current = current.next
        return len(patients) == self.capacity


patient1 = Patient("Ivan")
patient2 = Patient("Kolio")
patient3 = Patient("Mario")

op_room = OperatingRoom(3)

op_room.admit_patient(patient1)
op_room.admit_patient(patient2)
# op_room.admit_patient(patient3)

print(op_room.current_patients())
print(op_room.is_full())