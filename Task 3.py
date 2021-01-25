#!/usr/bin/env python
# coding: utf-8

# In[5]:


#1.Create a list of 10 elements of four different data types like int, string, complex and float.
list=[1, 3.5, 99, 'hi', 44.7, 5.5j, 'key', 21, 2.9, 7j]
print(list)


# In[8]:


#2.Create a list of size 5 and execute the slicing structure
list=[10,5,67,58,26]
print('list is :',list)
print('Slice the list :',list[0:3])


# In[13]:


#3.Write a program to get the sum and multiply of all the items in a given list.
list=[1,2,3,4]
n=len(list)
print('Sum of all the items in a given list is :', sum(list))
multiplication=1
for i in range(1,n+1):
    multiplication*=i
print('Multiplication of all the items in a given list is :', multiplication)


# In[15]:


#4.Find the largest and smallest number from a given list.
list=[54,62,31,28,94,57,-9,-0.5,191,1,0]
print('Largest number from a given list :', max(list))
print('Smallest number from a given list :', min(list))


# In[18]:


#5.Create a new list which contains the specified numbers after removing the even numbers from a predefined list.
list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
n=len(list)
print('List is :',list)
for i in range(n):
    if not list[i]%2==0:
        print(list[i])


# In[22]:


#6.Create list of elements such that it contains the squares of the first and last 5 elements between 1and30 (both included).
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
n=len(list)
list1=[]
print('List is :',list)
for i in range(n+1):
    if i in range(1,6) or i in range(26,31):
        list1.append(i**2)
print('List of elements such that it contains squares of first and last 5 elements between 1&30 is :',list1)


# In[26]:


#7.Write a program to replace the last element in a list with another list. Sample input: [1,3,5,7,9,10], [2,4,6,8]
#Expected output: [1,3,5,7,9,2,4,6,8]
list=[1,3,5,7,9,10]
list[-1:]=[2,4,6,8]
print(list)


# In[28]:


#8.Create a new dictionary by concatenating the following two dictionaries: Sample input: a={1:10,2:20} b={3:30,4:40}
#Expected output: {1:10,2:20,3:30,4:40}
def Merge(a,b):
    res={**a,**b}
    return res
a={1:10,2:20} 
b={3:30,4:40}
c=Merge(a,b)
print(c)


# In[30]:


#9.Create a dictionary that contain numbers in the form(x:x*x) where x takes all the values between 1 and n(both 1 and n 
#included). Sample input: n=5. Expected output: {1:1, 2:4, 3:9, 4:16, 5:25}
n=eval(input('Enter n value :'))
dict1=dict()
for i in range(1,n+1):
    dict1[i]=i*i
print(dict1)


# In[33]:


#10.Write a program which accepts a sequence of comma-separated numbers from console and generates a list and a tuple which 
#contains every number in the form of string. Sample input: 34,67,55,33,12,98
#Expected output: [‘34’,’67’,’55’,’33’,’12’,’98’] (‘34’,’67’,’55’,’33’,’12’,’98’)
sequence=input('Enter a sequence of comma-separated numbers : ')
list=print('Sequence in list :',sequence.split(','))
tuple=print('Sequence in tuple :',tuple(sequence.split(',')))


# In[ ]:




