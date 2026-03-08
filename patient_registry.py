class patient_registry:

    def __init__(self):
        self.patients = {}
        self.firstID = 100

    ### REQ-01: The system shall allow the creation of
    ### a new patient record with a name and a unique Patient ID.
    def register_patient(self, name):

        self.patients[self.firstID] = name
        self.firstID += 1

        return self.firstID - 1

    ### REQ-02: The system shall retrieve a patient's
    ### record using their unique Patient ID.
    def get_patient(self, patient_id):

        if patient_id in self.patients.keys():
            return {patient_id: self.patients[patient_id]}
        else:
            raise KeyError(f'ID# {patient_id} was not found in the registry!')

    ### REQ-04: The system shall allow updating a patient’s name using
    ### their Patient ID, while keeping the Patient ID unchanged.
    def update_patient_name(self, patient_id, new_name):

        if patient_id in self.patients.keys():
            self.patients[patient_id] = new_name
        else:
            raise KeyError(f'ID# {patient_id} was not found in the registry!')

    ### REQ-05: The system shall allow deleting a
    ### patient record using their Patient ID. If the ID
    ### does not exist, the system shall display
    ### an appropriate error message.
    def delete_patient(self, patient_id: str):


        if patient_id in self.patients.keys():
            self.patients.pop(patient_id)
            return True

            ### REQ-05: If the ID does not exist,
            ### the system shall display an appropriate error message.
        else:
            raise KeyError(f'ID# {patient_id} was not found in the registry!')


