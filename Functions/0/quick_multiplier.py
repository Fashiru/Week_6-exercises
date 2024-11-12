doubler = lambda n: n * 2


#Creating the doubler function with various inputs
print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

# Create the tripler variable
tripler = lambda n: n * 3

# Test the tripler function with various inputs
print(tripler(8))
print(tripler(-4))
print(tripler('banana'))

def multiplier(factor):
    return lambda n: n * factor



# Create multiplier variables with a sample value
quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)



#Display
print(quadrupler(3))
print(quintupler(3))
print(sextupler(3))
print(septupler(3))
print(octupler(3))
print(nonupler(3))
print(decupler(3))



