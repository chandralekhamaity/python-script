# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 17:19:34 2021

@author: CHANDRALEKHA
"""

integer = -67
abs(integer)
print('Absolute value of -67 is :',abs(integer))

floating = -57.9999
print('Absolute value of -57.9999 is :', abs(floating))

k = [1, 2, 3, 4, 5, 6, 7, 8]
print(all(k))

k = [2, False]
print(all(k))

k = [1, 3, 5, 7, 8]
print(all(k))

k = [1, 2, 4, 5, 0]
print(all(k))

k = []
print(all(k))

test = []
print(test, 'is', bool(test))

test = [0]
print(test, 'is', bool(test))

test = None
print(test, 'is', bool(test))

test = 'Enjoy'
print(test, 'is', bool(test))

test = 'easy string'
print(test, 'is', bool(test))

list_1 =[1,2,4]
s = sum(list_1)
print(s)

s = sum(list_1, 10)
print(s)

strA = 'Python'
print(len(strA))

Chavu = list()
print(Chavu)

String = 'reyansh'
print(list(String))

result = divmod(99,6)
print(result)

result =dict()
print(result)

result2 = dict(a=4,b=8)
print(result2)

result = set()
result2 = set('99')
result3 = set('rstudioprest')
result4 ={6,7}
print(result)
print(result2)
print(result3)
print(result4)

print(pow(99,88))

print(pow(-5,9))

print(pow(-99,88))

t1 = tuple()
print('t1=', t1)

l = [8,9,5]
t2 = tuple(l)
print('t2=', t2)

t1 = tuple('C++')
print('t1=', t1)

x = lambda a,b:a+b
print("Addition=", x(77,99))

List = [1,2,3,4,22,100,103,123]
Oddlist = list(filter(lambda x:(x%2==0), List))
print(Oddlist)

List = [1,2,3,4,17,66,100,123]
new_list = list(map(lambda x:x*4,List)) 
print(new_list)  
