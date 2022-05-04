# #EXERCISE 1
# # Filter out all of the empty strings from the list below

# # Output: ['Argentina', 'San Diego', 'Boston', 'New York']
places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

def a_places(place):
    if place and place[0]!=' ':
        return True
    else:
        return False
new_places_list = list(filter(a_places, places))
print(new_places_list)

# #-------OR---------

new_places_lamb = list(filter(lambda place: True if place and place[0]!=' ' else False, places))
print(new_places_lamb)



#EXERCISE 2
# Write an anonymous function that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"

# Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

sorted_author = sorted(author,key=lambda x: x.lower().split(" ")[-1])
print(sorted_author)



# # Exercise 3
# # Convert the list below from Celsius to Farhenheit, using the map function with a lambda...
# Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]
 # F = (9/5)*C + 32
 
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]
F = list(map(lambda x: (x[0],x[1]*9/5+32) ,places))
print(F)


# # Exercise #4
# Write a recursion function to perform the fibonacci sequence up to the number passed in.

# Output for fib(5) => 
# Iteration 0: 1
# Iteration 1: 1
# Iteration 2: 2
# Iteration 3: 3
# Iteration 4: 5
# Iteration 5: 8

def fibon(num):
    if num ==0 or num ==1:
        return 1
    else:
        return fibon(num-2) +fibon(num-1)

print(fibon(5))