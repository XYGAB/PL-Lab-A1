#Answers only

#Part 1
names = ["Alice","Bob","Charlie"] #missing comma between "Alice" and "Bob".
for name in names: #for loop requires a colon (:) at the end.
    print("Student:", name) #print function in Python needs commas to separate arguments
print("Done!") #Python is case-sensitive, the Print should be print.

#Part 2
x = "Global"

def outer():
    y = "outer local"
    def inner():
        print(x, y)
    inner()
    print(y)
outer()

'''By default, inner functions can only read outer variables, not modify them. The keyword nonlocal allows inner() to modify y from outer().
This way, the change persists after inner() is executed.'''

#Part 3
def combine(a: str, b: str):
    return a + b

print = (combine(3, 10))
print = (combine("Hi ", "Bob"))
print = (combine("Hi", 5))

'''Python allows + on integers for addition and strings concatenation. But str + int is not allowed, so we enforce type checking.
Type hints (a: int, b: int) help make code safer and more readable.'''

#Part 4
total = 0
for i in range(1, 5):
    total += i
print(total)

'''The semantic error was using range(1, 5) instead of range(1, 6). The range(1, 5) only includes 1, 2, 3, 4 (not 5).
This is not a syntax error because the program still runs without issues, but it produces the wrong meaning (logic) result.'''

#Part 5
numbers = [1, 2, 3, 4, 5, 6,]
result = []

for n in numbers:
    if n % 2 == 0:
        result.append(n ** 2)
print(result)

'''Uses a step-by-step sequence of instructions (loop + condition). This is imperative programming,
Sbecause we explicitly tell the computer how to compute the result.'''