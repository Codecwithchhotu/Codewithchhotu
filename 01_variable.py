# a=1   
# b=3
# c=a+b   # a,b=variable , 1,3=constant value
# # c=7
# print(a+b)
# print(c)
# c=7
# name="Arya"
# print(name)

# x = "100"
# y = 50
# y = str(y)
# # This will raise an error
# print(x + y)  # TypeError: can only concatenate str (not "int") to str

# x = "100"
# y = 50
# print(int(x) + y)  # Output: 150

# x = 50
# y = "25"
# print(str(x) + y)

# x = "50"
# y = "25"
# print(x+y)

# Set example
# s = {1, 4, 3}    #not works because esme kabel one argument ko he add kar sakte hai
# s.add(4,5,9,3)  # Works fine
# print(s)

s = {1, 4, 3}    #not works because esme kabel one argument ko he add kar sakte hai
s.add(0)  # Works fine
print(s)   #Add in accending order


s = {1, 4, 3}
s.update([4, 5, 9, 3])  # ✅ Works fine!
print(s)

# # Frozenset example
# fs = frozenset([1, 2, 3])
# # fs.add(4)  # Raises AttributeError because frozenset is immutable

# x = int("100")  # Convert x from string to integer
# y = 50          # Keep y as an integer
# print(x + y)    # 100 + 50 = 150

# x = "100"
# y = 50
# print(int(x) + y)  # Outputs: 150



# s = {1, 2, 3}
# s.add(4)


# s = {1, 2, 3}
# s.add(4)
# print(s)  # Outputs: {1, 2, 3, 4}


# s = {1, 2, 3}
# s.update([4, 5, 6])  # Ek saath multiple elements add karega
# print(s)  # Output: {1, 2, 3, 4, 5, 6}


#1
name = "Chhotu"
age = 20
price = 25.5
print("name")
print("age")
print("price")
print(name)
print(age)
print(price)

#2
name = "Chhotu"
age = 20                   #(Right)
price = 25.5               #(Right)                 
print("my name is:",name)
print("my age is:",age)
print("price is:",price)

#3
age2 = age
print(age)
print(age2)

#4
print(type(name))
print(type(age))  #(42,+54,-9) ,same answer not other answer
print(type(price))
