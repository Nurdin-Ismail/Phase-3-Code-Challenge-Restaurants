class Review:

    all1 = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = Review.validate_rating_initialization(rating)
        Review.add_review_to_all(self)

    @staticmethod
    def validate_rating_initialization(rating):
        if(type(rating) == int):
            return rating
        else:
            print("rating must be an integer")


    
    @classmethod
    def add_review_to_all(cls, review):
        cls.all1.append(review)
    
    @classmethod
    def all(cls):
        review = []
        return [
            {
                "Customer" : review.customer,
                "Restaurant" : review.restaurant,
                "Rating" : review._rating
            }
            
            for review in cls.all1]
    
    def get_rating(self):
        return self.rating 
    
    def validate_rating(self, rating):
        if(type(rating) == int):
            self.rating = rating
        else:
            return "rating must be an integer"
    
    rating = property(validate_rating, get_rating)
    @property
    def customer(self):
        return self._customer
    @property
    def restaurant(self):
        return self._restaurant
    


good = Review('John', "Pizza Inn", 5)
ron = Review('Johny', "Pizza Inn", 1)
not_bad = Review('Lee', "Burger King", 2)
bad = Review('Kanu', "Art Cafe", 4)
lod = Review('leni', "Pizza Inn", 7)
not_good = Review('Mercy', "Alcheno", 9)
good = Review('Kon', "Pizza Inn", 5)
good = Review('Jo', "Pizza Inn", 5)
good = Review('Mon', "Pizza Inn", 5)
good = Review('Kohn', "Pizza Inn", 5)
good = Review('Lohn Doe', "Pizza In", 5)


# print(Review.all())


# print(good.all())
# # good.restaurant = "alcheno"
# print(not_good._rating)
