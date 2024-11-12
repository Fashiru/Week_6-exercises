name = None 
while name == None:
    try:
        name = input('Name?').lower()

        int(name)
    except:
        
        if len(name) < 2:
            print("Not a valid name(must be 2 or more letters)")
            name = None 
        else:
            print(f"Hello, {name}!") 



n2 = None
while n2 == None:
    try:
        n2 = name[1] 
    except IndexError:

        print("Not a valid name (must be 2 or more letters)") 
        raise SystemExit(0)
    else:
        print(f"Name second character: {n2}")

print(f"Final Valid name: {name}")
                        