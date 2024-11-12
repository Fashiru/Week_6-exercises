class RewardsProgram:


    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email
        self.restaurant_visited = []
        self.rewards_points = {}

    def profile(self):
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")   

    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")


    def add_to_cust_list(self):
        cust_list.append((self.cust_name, self.phone, self.email))

    def visit_rest(self):
        restaurant = input("Name of restaurant: ")
        if restaurant not in self.restaurant_visited:
            self.restaurant_visited.append(restaurant)    
          
        total_bill = float(input("What was the total food bill for this visit? $"))         
        points = self.calculate_rewards(total_bill) 

        if restaurant not in self.restaurant_visited:
            self.rewards_points[restaurant] = 0
        self.rewards_points[restaurant] += points


    
        print(f"Points for this visit: {points}")
        print(f"Total rewards points earned: {self.rewards_points[restaurant]}")
        print(f"Thank you for visiting {restaurant}")


        def calculate_rewards(self, total_bill):
            return int(total_bill)
        
     #Create instances   
customer1 = RewardsProgram("Alice Smith", "555-1234", "alice.smith@gmail.com")
customer1.visit_rest()
customer1.visit_rest()

customer2 = RewardsProgram("John Cena", "123-123", "youcantseeme@gmail.com")
customer2.visit_rest()


print("\nRewards Points by Restaurant:")
print(customer1.rewards_points)
print(customer2.rewards_points)