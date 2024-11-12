def parse_and_display(name):
    
    # find the space in the name
    space_index = name.find(' ')


    #Extract first and last names
    first_name = name[ :space_index]
    last_name = name[space_index + 1:]


    #Display
    print(f"Full Name: {name}")
    print(f"First Name: {first_name}")
    print(f"Last Name: {last_name}")


    #Test function with different names
parse_and_display('Abel Tesfaye')
parse_and_display('Ryan Renolds')
parse_and_display('Steph Curry')
parse_and_display('Lorde')
parse_and_display('Billie Eilish')
parse_and_display('Megan Thee Stallion')






