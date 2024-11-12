class Restaurant:

    def __init__(self, rest_name, food_type):

        self.rest_name = rest_name
        self.food_type = food_type


    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")    


class FoodTruck(Restaurant):


     def __init__(self, rest_name, food_type):
        super().__init__(rest_name, food_type)
        self.private_bookings = 'N'
        self.truck_location = ''
        self.location_history = []

     def accepts_private_bookings(self):
       self.accepts_private_bookings = input("Does this food truck accept private bookings? Y/N:")    
            