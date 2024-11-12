

try:
    m = banana
except NameError:
    print("NameError: Oops, looks like you tried to assign an undefined object to a variable")
else: 
    print(m)
finally:
    print("Let's try another one....")


#ValueError
try:
    x = int("hello")
except ValueError:
    print("ValueError: You tried to convert a non-numeric string to an integer.") 
else:
    print("x =", x)
finally:
    print("Let's try another one...")

#NameError
try:
    m = banana 
except NameError:
    print("NameError: Oops, looks like you tried to assign an undefined object to a variable.")  
else:
    print("m=", m)
finally:
    print("Let's try another one....")

#TypeError
try:
    y = "string" + 10
except TypeError:
    print("TypeError: You can't combine a string and an integer.")   
else:
    print("y=", y)  
finally:
    print("Let's try another one....")       

#SyntaxError
try:
    eval('x === 10')
except SyntaxError:
    print("SyntaxError: There is a mistake in the syntax of your code.")
else:
    print("The code ran without any syntax errors.")
finally:
    print("Lets try another one...")            