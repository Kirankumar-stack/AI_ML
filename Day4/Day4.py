#!/usr/bin/env python
# coding: utf-8

# Question 1 :
# Research on whether addition, subtraction, multiplication, division, floor division and modulo
# operations be performed on complex numbers. Based on your study, implement a Python
# program to demonstrate these operations.
# 

# In[3]:


num1= 1+5j
num2 = 4+8j
sum = num1+num2
print('sum =',sum)
sub =num1-num2
print('sub =',sub)
mul = num1 *num2
print('mul =',mul)
div = num1/num2
print('div=',div)


# In[8]:


import cmath
print(num1.real)
print(num1.imag)
print(num1.conjugate())
print(abs(num1))


# Question 2 : Research on range() functions and its parameters. Create a markdown cell and write in your own words (no copy-paste from google please) what you understand about it. Implement a small program of your choice on the same.
# 

# In[47]:


data= range(1,25)

for i in data:
    if(i%2==1):
        print(i)
print("odd nunbers printed")


# In[ ]:


Question 3:  Consider two numbers. Perform their subtraction and if the result of subtraction is greater than 25, print their multiplication result else print their division result


# In[26]:


fnum = 90 #intput()
snum = 70 #intput()  #int(int())

subb= fnum-snum
#print(fnum*snum)

if(subb >= 25):
    print(int(fnum*snum) )
else:
    print(fnum/snum)


# In[28]:


fnum = 80
snum = 55   #int(int())

subb= fnum-snum

if(subb >= 25):
    print(fnum*snum )
else:
    print(fnum/snum)


# Question 4: Consider a list of 10 elements of integer values. If the number in the list is divisible by 2, print the result as "square of that number minus 2".

# In[45]:


elem =[2,4,5,6,7,8,9,2,4,7]

print(elem[4])

for i in elem:
    if(i%2==0):
        print(i**2 -1)
       

        


# Question 5: Consider a list of 10 elements. Print all the elements in the list which are greater than 7 when that number is divided 2. 

# In[50]:


elemets = [2,3,5,6,7,8,9,7,8,12]

for i in elemets:
    if(i>7):
        if(i%2 == 0):
            print(i)
        


# In[ ]:




