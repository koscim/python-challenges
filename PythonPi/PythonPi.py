"""
Name: PythonPi.py
Purpose: Get the value of Pi to n number of decimal places
Author: Monica Kosciuk (koscim)

"""

print 'Hello, World!'
name = raw_input('What is your name?\n')
print 'Hi, %s.' % name

friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print "iteration {iteration} is {name}".format(iteration=i, name=name)

parents, babies = (1, 1)
while babies < 100:
    print 'This generation has {0} babies'.format(babies)
    parents, babies = (babies, parents + babies)

def greet(name):
    print 'Hello', name
greet('Jack')
greet('Jill')
greet('Bob')
