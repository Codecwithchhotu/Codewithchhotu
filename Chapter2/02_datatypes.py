a=1      # a is an integer

b=5.22   # b is a floating point number

c="Arya" # c is a string

d=False or True  # d is a boolean 

e="none "  # e is a none type variable
        

#1
name1  = "sk"
name2  = 'sk'
name3  = '''sk'''
print(name1)
print(name2)
print(name3)
print("name3")

#2
# age = 23
# old = False/True
# a= None
# print(type(old))
# print(type(a))

# old = False/True – This line is problematic because it’s not valid Python syntax. It’s as if you’re trying to assign both False and True to old simultaneously, which isn’t possible. You should assign old to either False or True. For example:


# age = 23
# old = False/True
# a = None
# print(type( old))  
# old = False/True: This line evaluates the expression False/True. Since False is equivalent to 0 and True is equivalent to 1 in Python, this essentially translates to 0/1, which equals 0.0 (a floating-point number). The correct interpretation of this line should be that old is assigned the floating-point value 0.0, not a boolean value.



age = 23
old = False
a = None
print(type(old))
print(type(a))
print(type(old))


age = 23
old = True
a = None
print(type(old))
print(type(a))
print(type(old))

#3
a = 2
b = 5
# sum = a+b
# print(a+b)
print(a+b)
#4
a = 500
b = 200
diff = a-b
print(diff)

