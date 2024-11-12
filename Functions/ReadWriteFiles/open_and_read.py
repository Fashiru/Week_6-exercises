
with open('about_me.txt', 'r') as f:
    content = f.read()
    print(content)


with open('about_me.txt', 'r') as f:
    print(f.read(50))
    print(f.read(50))


with open ('about_me.txt', 'r') as f:
    print(f.readline(10))
    print(f.readline())     


    for i in range(1, 5):
        print(f.readline())

with open('about_me.txt', 'r') as f:
    print(f.readlines(1))
    print(f.readlines(10))
    print(f.readlines(100))
    print(f.readlines(-1))



with open('about_me.txt', 'r') as f:
    first_50_chars = f.read(50)
    lines = [f.readline().strip() for _ in range(4)]
    next_100_chars = f.read(100)


print("First 50 characters:", first_50_chars) 
print("Next four lines, as list by line:", lines)
print("Next 100 characters:", next_100_chars)

