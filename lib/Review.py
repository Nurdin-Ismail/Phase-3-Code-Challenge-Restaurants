class Review:

    all1 = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self._rating = rating
        Review.add_review_to_all(self)



        
    def get_just_rating(self):
        return self.rating
    
    @classmethod
    def add_review_to_all(cls, review):
        cls.all1.append(review)
    
    @classmethod
    def all(cls):
        
        return ["Customer:" + ' '  + review.customer + ' ' + ',' + "Restaurant:" + ' ' + review.restaurant + ' ' + ',' + "Rating:" + str(review.rating) for review in cls.all1]
    
    def get_rating(self):
        return self._rating 
    
    def validate_rating(self, rating):
        if(type(rating) == int):
            self._rating = rating
        else:
            print("rating must be an integer")
    
    rating= property(get_rating, validate_rating)
    


good = Review('John', "Pizza Inn", 5)
not_bad = Review('Lee', "Burger King", 2)
bad = Review('Kanu', "Art Cafe", 4)
not_good = Review('Mercy', "Alcheno", 'three')

print(good.all())

print(good.rating)
