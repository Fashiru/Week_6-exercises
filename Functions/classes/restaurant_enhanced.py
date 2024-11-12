class Restaurant:


    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []



    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")


    def rest_open(self):
        print(f"{self.rest_name} is open.")        

    def add_num_served(self):
        try:
            customers = int(input("How many customers served today? "))
            self.number_served += customers
        except ValueError:
            print("Please enter a valid number.")    


    def print_num_served(self):

        print(f"{self.rest_name} has served {self.number_served} customers.")

    
    def customer_rating(self):

        while True:
             try:
                rating = int(input("How would you rate your experience today on a scale of 1-5? "))    
                if rating < 1 or rating > 5:
                    print("Please enter a valid rating betweeen 1 and 5")
                    continue
                self.customer_ratings.append(rating)
                avg_rating = sum(self.customer_ratings) / len(self.customer_ratings)
                print(f"Your rating was {rating}. The average rating for this restuarant is {avg_rating:.2f}.")
                break
             except ValueError:
                 print("Invalid input! Please enter an integer between 1 and 5.")

  # Create instances
restaurant_1 = Restaurant("Burger joint", "American")   
restaurant_2 = Restaurant("Sushi Spot", "Japanese")
restaurant_3 = Restaurant("Pizza Place", "Italian")

#Test the methods
restaurant_1.describe_rest()
restaurant_1.rest_open()
restaurant_1.print_num_served()
restaurant_1.add_num_served()
restaurant_1.print_num_served()
restaurant_1.customer_rating()


restaurant_2.describe_rest()
restaurant_2.rest_open()
restaurant_2.print_num_served()
restaurant_2.add_num_served()
restaurant_2.print_num_served()
restaurant_2.customer_rating()


restaurant_3.describe_rest()
restaurant_3.rest_open()
restaurant_3.print_num_served()
restaurant_3.add_num_served()
restaurant_3.print_num_served()
restaurant_3.customer_rating()

