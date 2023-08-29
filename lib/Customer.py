class Customer:

    all1 = []

    def __init__(self, first_name, last_name):

        self.first_name =first_name
        self.last_name = last_name
        Customer.add_customer_to_all(self)

    def given_name(self):
        
        return self.first_name
    
    def family_name(self):
       
        return self.last_name

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    

    @classmethod
    def add_customer_to_all(cls, customer):
        cls.all1.append(customer)

    @classmethod
    def all(cls):
        return [customer.first_name for customer in cls.all1]
    

john = Customer('John', 'Doe')
lee = Customer('Lee', 'Doe')
kanu = Customer('Kanu', 'Doe')
mercy = Customer('Mercy', 'Doe')

print(john.family_name())
print(john.full_name())

john.first_name = 'Johny'
print(john.full_name())

print(john.all())


