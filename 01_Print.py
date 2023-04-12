# import this

greet = 'Hello fuck'
extended_greet = 'Hello fuck, ' + 'fucking fuck'

name = 'Cristian'

personalized = f'Hello {name}'

greet_format = 'hello {}'

formatted = greet_format.format(name)

print(personalized)
print('#####')
print(formatted)
print('#####')
print(extended_greet, greet_format)
print('#####')
print(formatted.upper(), formatted.lower(), greet_format.upper())
print('#####')
print(formatted.replace('Cristian', 'Pol').upper())


