from Review import Review

class Customer:

    all1 = []

    def __init__(self, first_name, last_name):

        self.first_name =first_name
        self.last_name = last_name
        self.full_name = Customer.full_name1(self)
        Customer.add_customer_to_all(self)

    def given_name(self):
        
        return self.first_name
    
    def family_name(self):
       
        return self.last_name
    
    @staticmethod
    def full_name1(self):
        return f'{self.first_name} {self.last_name}'
    
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    

    @classmethod
    def add_customer_to_all(cls, customer):
        cls.all1.append(customer)

    @classmethod
    def all(cls):
        return [customer.first_name for customer in cls.all1]
    

    def restaurant(self):
        reviews = Review.all()
        new_count = 0
        restaurants = []
        all_restaurants = []

        for j in reviews:

            if j['Customer'] == self.first_name or j['Customer'] == self.full_name():
                new_count += 1
                obj = {
                    'id' : new_count,
                    'Restaurant' : j['Restaurant'],
                    
                }

                restaurants.append(obj)

                for i in restaurants:
                    for value in i.values():
       
        
                         

                          if value not in all_restaurants and type(value) == str:
                              all_restaurants.append(value)

        return all_restaurants
    
    def num_reviews(self):
        reviews = Review.all()
        new_count = 0
        restaurants = []
        

        for j in reviews:

            if j['Customer'] == self.first_name or j['Customer'] == self.full_name():
                new_count += 1
                obj = {
                    'id' : new_count,
                    "Customer" : j['Customer'],
                    'Restaurant' : j['Restaurant'],
                    'Rating' : j['Rating']

                    
                }

                restaurants.append(obj)

              
        print(len(restaurants))
        return len(restaurants)
    


    # @classmethod
    # def show_name(cls):
    #     names_list = [customer.full_name for customer in cls.all1]
        
        
    @classmethod
    def find_by_name(cls, name):
        names_list = [customer for customer in cls.all1]
        for i in names_list:
            if i.full_name == name:
                obj = { 
                         'Name' : i.full_name,
                         'Customer Instance' :  i,
                }
                return obj
                
            else:
                continue
                return 'Customer Does Not Exist'
                

    @classmethod
    def find_all_by_given_name(cls, name):
        names_list = [customer for customer in cls.all1]
        new_list = []

        for i in names_list:
            if i.first_name == name:
                obj = {
                    'Name': i.first_name,
                    'Customer Instance' : i
                }
                new_list.append(obj)
            else:
                continue
        return new_list   


    

john = Customer('John', 'Doe')
lee = Customer('Lee', 'Doe')
kanu = Customer('Kanu', 'Doe')
mercy = Customer('Mercy', 'Doe')
mercy = Customer('Mercy', 'Doe')
mercy = Customer('Mercy', 'Doe')
mercy = Customer('Mercy', 'Doe')
print(Customer.find_by_name('Kanun Doe'))
print(Customer.find_all_by_given_name('Mercy'))

# print(john.family_name())
# print(john.full_name())

# john.first_name = 'John'
# print(john.full_name())

# print(john.all())

# print(john.restaurant())
# print(john.num_reviews())


