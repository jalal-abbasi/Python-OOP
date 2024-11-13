class Clinic(object):
    
    max_patients = 3
    
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.waiting_list = []
    
    def add_patient(self, patient):
        if len(self.patients) :
            self.waiting_list.append(patient)
        else:
            self.patients.append(patient)

my_clinic = Clinic(None)
my_clinic.add_patient("Danny")
print()
