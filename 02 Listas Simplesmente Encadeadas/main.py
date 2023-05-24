class Patient():
    def __init__(self,id,name,health_Status):
        self.id = id
        self.name = name
        self.health_status = health_Status
        self.next_patient = None

class ListPatient():
    def __init__(self):
        self.head = None

    