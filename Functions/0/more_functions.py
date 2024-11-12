def displaying_mailing_label(name, address, city, state, zip_code):
    print(f"{name}")
    print(f"{address}")
    print(f"{city}, {state} {zip_code}")


displaying_mailing_label("Fadil Ashiru", "727 E Elmurst Street", "Chicago", "Illinois", "60637")
displaying_mailing_label("Peter Parker", "2506 Spiderman lane", "Brooklyn", "New york", "40265")

def add_numbers(*numbers):
    total = sum(numbers)
    results = ' + '.join(map(str, numbers)) + f" = {total}"
    print(results)
 
add_numbers(5)   
add_numbers(10,20)
add_numbers(2, 3, 4, 5, 6)



def display_receipt(total_due, amount_paid):
    print(f"Total Due: ${total_due:.2f}")
    print(f"Amoumt Paid: ${amount_paid:.2f}")     
    if amount_paid > total_due:
        change_due = amount_paid - total_due
        print(f"Change Due: ${change_due:.2f}")
    elif amount_paid == total_due:
        print("No change due.")
    else:
        balance_due = total_due - amount_paid
        print(f"Balance Due: ${balance_due:.2f}")        
    print()    

display_receipt(100, 120)
display_receipt(50,50)
display_receipt(30, 20)
