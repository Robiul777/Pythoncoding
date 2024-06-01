# """
# a=22
# b=45
# print(a-b)
# """
# # print("max")
# a=input()

# print(a)

# # multiple value in multiple variable
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
x=y=z= "Orange"
print(z)
print(y)


# Unpack a Collection
country=["india", "nepal", "bangladesh"]
a, b, c= country
print(a)
print(b)
print(c)

# output variable, we can add using comma, and plus
x="my "
y="name "
z="is "
w="robi "
print(x ,y ,z ,w)
# Or
print(x +y +z +w)

# Global Variables
x="awesome"

# global keyword
def myfunc():
    global x
    x="awesome"
myfunc()
print("python is", x)

