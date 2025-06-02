a=31
t=type(a) # class <int>
print(t)

a = 31
t = type
print(t)

a=31.2
t=type(a)  # class<float>
print(t)

a=23
old=False
a=None
print(type(old))
print(type(a))

a="herry"
t=type(a)  # Class<str>
print(t)

a="31.2"
t=type(a)  # class<str>
print(t)


a="31.2"
b=float(a) # a but the type should be float
t=type(b)
print(t)
