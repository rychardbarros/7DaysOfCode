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
            # Se a lista estiver vazia, o novo paciente é adicionado como cabeça da lista
            self.head = new_patient
        else:
            # Caso contrário, o paciente é adicionado ao final da lista
            present_patient = self.head
            while present_patient.next_patient is not None:
                present_patient = present_patient.next_patient
            present_patient = new_patient

    # Método para remover um paciente da lista, recebe como parâmetro o id do paciente a ser removido
    def remove_patient(self, id):
        if self.head is None:

            return

        elif self.head.id == id:
            # Se o paciente a ser removido for a cabeça da lista, basta atualizar o ponteiro para o próximo paciente
            self.head = self.head.next_patient
            return

        else:
            # Caso contrário, percorremos a lista até encontrar o paciente a ser removido
            present_patient = self.head
            while present_patient.next_patient is not None:
                if present_patient.next_patient.id == id:
                    # Quando encontramos o paciente, atualizamos o ponteiro do paciente anterior para o próximo paciente
                    present_patient.next_patient = present_patient.next_patient.next_patient
                    
