user_name = input("Enter a name: ").strip

def trunc_name(name):
    name = name.lower()
    vowels = "aeiou"

    if name[0] in vowels:
        return name
    elif len(name) > 1 and name[1] not in vowels:
        return name[1:] # if the name starts with two consonants, remove the first twp
    else:
        return name[1:] # Otherwise, remove the first character
    

#Test trunc_name function
print(trunc_name("Ann"))
print(trunc_name("Dan"))
print(trunc_name("Stan"))
print(trunc_name("Aidan"))
print(trunc_name("BRADEN"))

# Generator with special function
def name_game(name):
    naughty_names = ['bart', 'buck']
    if name.lower() in naughty_names:
        print("Warning: This game is not allowed in the Name Game!")

    truncated_name = trunc_name(name)



    yield f"{name}, {name}, bo-{truncated_name}"    
    yield f"banana fana fo-{truncated_name}"
    yield f"me my mo-{truncated_name}"
    yield f"{name}!"


names_to_test = ["carly", "CHARLIE", "Aidan", "Braden", "Billy Bob"]    

#Loop through each name and print song
for name in names_to_test:
    print(f"--- Name Game for {name} ---")
    for line in name_game(name):
        print(line)
    print()

def name_game(name):

    truncated_name = trunc_name(name)
    

    if name [0].lower() in ['b', 'f', 'm']:
        special_prefix = name[0].lower() + 'a'
    else:
        special_prefix = 'bo'    

    yield f"{name}, {name}, {special_prefix}-{truncated_name}"     
    yield f"banana fana fo-{truncated_name}"
    yield f"me my mo-{truncated_name}"
    yield f"{name}"

