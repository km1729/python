'''
getattr()
'''
#getattr(obj, attr_name, defalut)
class Student:
    name = "Kelly"
    marks = 88

person = Student()

name = person.name
name2 = getattr(person,'name','who')
name3 = getattr(person,'name2','who')
print("=============== getattr")
print('name: '+name)
print('name2: '+name2)
print('name3: '+name3)

'''
output:
name: Kelly
name2: Kelly
name3: who
'''


#setattr(obj, attr_name, value)
print("=============== setattr")
setattr(person, 'gender', 'F')
print(person.gender)

'''
output:
F
'''

#hasattr(obj, attr_name)
print("=============== hasattr")
print(hasattr(person, 'name'))
print(hasattr(person, 'name2'))

'''
output:
True
False
'''

#delattr(obj, attr_name)
print("=============== delattr")
print(hasattr(person, 'gender'))
delattr(person,'gender')
print(hasattr(person, 'gender'))

'''
output:
True
False
'''

#dir(obj) print all avaialbe attribute
print("=============== dir()")
print(dir(person))


'''
output:
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', 
'__init__', '__init_subclass__', '__le__', '__lt__', '__module__', 
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 
'marks', 'name']
'''
    
# Better comment extention test
# //TODO: example
# //OPTIMIZE
# //FIXME