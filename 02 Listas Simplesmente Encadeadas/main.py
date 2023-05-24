# Definindo a classe Paciente para representar o nó da lista
class Patient():
    def __init__(self,id,name,health_status):
        self.id = id
        self.name = name
        self.health_status = health_status
        self.next_patient = None

# Definindo a classe ListaDePacientes para representar a lista simplesmente encadeada
class ListPatient():
    def __init__(self):
        self.head = None

    def add_patient(self, id, name ,health_status):
        new_patient = Patient(id, name, health_status)
        if self.head is None:
            self.head = new_patient
        else:
            present_patient = self.head