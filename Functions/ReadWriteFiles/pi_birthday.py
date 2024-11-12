
with open("pi_million_digits.txt", 'r') as pi:
    first_line = pi.readline()
    print(first_line)

with open('pi_million_digits.txt', 'r') as pi:

    pi_lines = pi.readline()

print("First 500 of pi:", ''.join(pi_lines)[:500])


user_birthday = input("Enter your birthday in format MMDDYY: ")

birthday_found = None

with open('pi_million_digits.txt', 'r') as pi:
    pi_lines = pi.readlines()

    for line in pi_lines:
        if user_birthday in line:
            print("Your birthday is in the first million digits of pi.")
            birthday_found = 1
            break


    if birthday_found != 1:
        print("Sorry, your birthday was not in the first million digits of pi.")  





with open('pi_million_digits.txt', 'r') as pi:
    pi_lines = pi.readlines()

    print(f"First line: {pi_lines[0]} (length: {len(pi_lines[0])})")    
    print(f"Second line: {pi_lines[1]} (length:{len(pi_lines[1])})")  


pi_string = ''
for line in pi_lines:
    pi_string += line.strip()


if birthday_found == 1:
    birthday_position = pi_string.index(user_birthday) - 1
    print(f"Your birthday begins at decimal place {birthday_position}.")    



  