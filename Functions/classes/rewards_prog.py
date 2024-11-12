cust_list = []


class RewardsProgram:


    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

    def profile(self):

        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")


    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant")


    def add_to_cust_list(self):
        cust_list.append((self.cust_name, self.phone, self.email))            


  #Create three instances of rewards program
customer_1 = RewardsProgram("Clark Kent",  "543-210", "clark.kent@gmail.com")      
customer_2 = RewardsProgram("Bruce Wayne", "012-345", "bruce.wayne@gmail.com")
customer_3 = RewardsProgram("Peter Parker", "765-432", "peter.parker@gamil.com")

#Run the method 
customer_1.profile()
customer_1.thank_you()
customer_1.add_to_cust_list()

customer_2.profile()
customer_2.thank_you()
customer_2.add_to_cust_list()

customer_3.profile()
customer_3.thank_you()
customer_3.add_to_cust_list()

print("\nCustomer List:")
print(cust_list)