class Worker:

    def __init__(self, name='Ivan', surname='Ivanov', position='manager', wage=500, bonus=150):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_salary(self):
        return self._income['wage'] + self._income['bonus']


v_pet = Position('Ivan', 'Ivanov', 'sales manager', 600, 180)
print(f'New attributes are: {v_pet.name}, {v_pet.surname}, {v_pet.position}, {v_pet._income}')
print(f'Total salary of {v_pet.get_full_name()} is {v_pet.get_full_salary()}')