# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 17:26:36 2021

@author: CHANDRALEKHA
"""

print("hare krishna")

#Numbers
#a=3 , b=5  #a and b are number objects 

#string
str1 = 'Hare Krishna'
str2 = 'Radhe Radhe'
str1
str2
print(str1[0:5])
(str1[0:5])
print(str1[8])
print(str1[2])
print (str1*2)
print (str1 + str2)

#list
l = [1,"Maa","Dad", False]
print (l[:3])
print (l[0:2])
print (l[3:])
print (l)
print (l + l)
print (l*3)
print (type(l))
#Lets try mutation 
l[0] = 'Tuktuk'
print(l)

#tuple
t = ('lion', 'tiger', 5 , 6)
t
print (t[:1]);
print (t[1:]);
print (t[0:3]);
print (t);
print (t + t)
print (t*4)
print (type(t))
#Lets try mutation
t[1] = "Giraffe"
print (t)

#dictionary
d = {1:"Chavu", 2:"Reyansh", 3:"Rohit", 4:"Mishu"}
d
print ("1st name is" +d[3])
print ("4th name is" +d[1])
print (d);
print (d.keys());
print (d.values());

#----ADVANCED----
#list
#ordered collection of items; sequence of items in a list
shoplist = ['veggies','fruits','candy','toiletries','essential']
shoplist
len(shoplist)
print(shoplist)

#add item to list
shoplist.append('clothes')
shoplist

#sort
shoplist.sort()  #inplace sort
shoplist

#index/select
shoplist[0]
shoplist[0:4]

#delete item
del shoplist[0]
shoplist

#Tuple
#Used to hold multiple object; similar to lists; less functionality than list
#immutable - cannot modify- fast ; ( )
zoo = ('zebra','elephant','deer','monkey')
zoo
len(zoo)
languages = 'c++','java','rstudio','py',7
languages
type(languages)

#Dictionary - like an addressbook. use of associate keys with values
#key-value pairs { 'key1':value1, 'key2':value2} ; { } bracket, :colon
students ={'A101':'AARUSH', 'A102':'PRINCE', 'A103':'CHINU', 'A104':'VISHAL'}
students
students['A103']
print('Name of rollno A103 is ' +students['A102'])
del students['A104']
students
len(students)

#for rollno, name in student.items():
    #print('name of {} is {} '.format(rollno, name) )

#Lets test Mutation: 
#adding a value
students['A104'] = 'Hadu'
students

#sets
Ram = {1,2,3,4,5,6,7.8}
Ram
Sham_2 = ()
Sham_2

#Sets are unordered collections of objects; ( [ , ])
teamA = set(['india', 'america', 'russia', 'france'])
teamA
teamB = set(['pakistan', 'china', 'turkey', 'iraq'])
teamB

#Checking whether a data value exists in a set or not.
'russia' in teamA
'russia' in teamB

#Adding values in a set
teamA.add('australia')
teamA #puts in orders
teamA.add('france')
teamA
teamA.remove('america')
teamA

#Create dataframe :
import pandas as pd

#Create a DataFrame
d = {'Name':['TUKTUK','CHINU','VISHAL','HADU','PRINCE','PIYUSH',
             'AARUSH','PRIYANKA','CHAVI','REYANSH','SIDDHARTH','SEENU'],
        'Exam':['Semester 1','Semester 1','Semester 1','Semester 1','Semester 1','Semester 1',
                 'Semester 2','Semester 2','Semester 2','Semester 2','Semester 2','Semester 2'],
            'Subject':['Mathematics','Mathematics','Mathematics','Science','Science','Science',
                             'Mathematics','Mathematics','Mathematics','Science','Science','Science'],
                                 'Score':[62,47,55,74,31,77,85,63,42,67,89,81]}

d

df = pd.DataFrame(d,columns=['Name','Exam','Subject','Score'])
df

#View a column of the dataframe in pandas:
df['Name']

#View two columns of the dataframe in pandas:
df[['Name','Score','Exam']]

#View first two rows of the dataframe in pandas:
df[0:2]
