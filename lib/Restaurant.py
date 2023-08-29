from Review import Review

class Restaurant:
    def __init__(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    
    
    def reviews(self):
        all2 = Review.all()
        
        count = 0
        review_land = []
        print(all2)
        new_count = 0
        for j in all2:
            count += 1
            
            print(j)
            if j['Restaurant'] == self.name:
                new_count += 1

                obj = {
                    'id' : new_count,
                    'Customer' : j['Customer'],
                    'Rating' : j['Rating']
                }

                review_land.append(obj)

            
        return review_land
    
    
    def customers(self):
        all2 = Review.all()
        value2 = []
        customers = []
        print(all2)
        new_count = 0
        for j in all2:
           
            
            print(j)
            if j['Restaurant'] == self.name:
                

                obj = {
                    'id' : new_count,
                    'Customer' : j['Customer'],
                    
                }
                
                customers.append(obj)

                for j in customers:
                      for value in j.values():
       
        
                          print(value)

                          if value not in value2 and type(value) == str:
                              value2.append(value)

                          print(value2)
                              
 
    

                
        return value2
                
    def average_star_rating(self):
        all2 = Review.all()
        rating_list = []
        for j in all2:
            
            
            print(j)
            if j['Restaurant'] == self.name:
                

                

                rating_list.append(j['Rating'])
        
        return round(sum(rating_list) / len(rating_list), 1)


            


        # return Review.all()
    
pizza = Restaurant('Pizza Inn')
print(pizza.reviews())
print(pizza.customers())
print(pizza.average_star_rating())
    


    
