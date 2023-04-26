# import this

greet = 'Hello fuck'
extended_greet = 'Hello fuck, ' + 'fucking fuck'

name = 'Cristian'

personalized = f'Hello {name}'

greet_format = 'hello {}'

formatted = greet_format.format(name)

#   print(personalized)
#   print('#####')
#   print(formatted)
#   print('#####')
#   print(extended_greet, greet_format)
#   print('#####')
#   print(formatted.upper(), formatted.lower(), greet_format.upper())
#   print('#####')
#   print(formatted.replace('Cristian', 'Pol').upper())
#   print('#####')


#############
#### LISTS
#############

names = ['Ursu', 'Pete', 'Cris', 'Eric']
ages = [32, 37, 33, 40]

# define vars and give them value of ordered element in list
ursu = names[0]
cris = names[2]

# tale everything at left of [2] 
ursuPete = names[:2]

# take 2nd 2 names
crisEric = names[2:]

# reverse the list [start:stop:step]
reverse = names[::-1] 

# every two
everyother = names[::2]

# get sum of all ages
allages = sum(ages)

# get min of ages
minage = min(ages)

# get max of ages
maxage = max(ages)


#############
#### LOOPS
#############

# while loop
print(':: While loop')
i = 0
while i < len(names):
    print(names[i], ages[i])
    i += 1

# for loop, less prone to bug, moe readable
print(':: For Loop')
for name in names:
    print(name)

# for loop using zip which doesn't buil a new list in memory
print(':: For Loop using zip')
for name, age in zip(names, ages):
    print(f"{name} {age}")

# print reverse list usind method
print(':: Use reversed method')
for name in reversed(names):
    print(name)

# print range that's not built in memory
for i in range(5):
    print(i)

# enumerate
print(':: For Loop to enumerate long list, 0-indexed')
for i, name in enumerate(names):
    print(f"{i} {name}")
