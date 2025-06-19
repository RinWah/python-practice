a_number = 5
another_number = 5.3
my_name = "rin"
many_numbers = [2, 5, 7, 23, 1, 4, 10]
more_numbers = range(10)

# check data type using the type() function
print(type(a_number))
print(type(another_number))
print(type(my_name))
print(type(many_numbers))
print(type(more_numbers))

# prints out #'s from 0-9
for item in range(10):
    print(item)

for item in more_numbers: # same as for item in range(10):
    print(item)

# won't work since it's not iterable -- aka can't iterate through its elements like a list, same with another_number
# for item in a_number: # a_number is an int
#     print(item)

for item in my_name: # iterable
    print(item)
