# string slicing
a="I am robiul"
print(a[1:6])
print(a[:])
print(a[-3:-1])

b = "Hello, World!"
print(b[-5:-2])

# Modify string
a="i  am robiul "
print(a.upper())
print(a.strip())
print(len(a))
print(a.endswith("mac"))
print(a.replace("robiul", "max"))
print(a.find("am"))
print(a.capitalize())
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']  so split() returns a list
print(a.casefold())

txt = "banana"

print(txt.center(11))


# String Concatenation
a="mac"
b="max"
c=a+" "+b
print(c)


# string format
age = 36
txt = f"My name is John, I am {age}"
print(txt)


