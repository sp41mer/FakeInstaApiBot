__author__ = 'sp41mer'
a = ['a','b','d','e','f']
b = ['b','d','e','f','g']
string = " ".join(str(x) for x in a)
list_s = string.split()
print(string)
print (set(a) -set(b))
print (set(b) - set(a))
