#!/usr/bin/env python
# coding: utf-8

# 
#  Question 1 : Write a program to subtract two complex numbers in Python

# In[5]:


a = 1+3j
b = 5+7j
sum = a+b
sum


# Question 2 : Write a program to find the fourth root of a number. 

# In[7]:


a=int(input())
b=a**4
b


# Question 3: Write a program to swap two numbers in Python with the help of a temporary variable.

# In[9]:


a=4
b=6
c=b
b=a
a=c
print(b)
print(a)


# Question 4: Write a program to swap two numbers in Python without using a temporary variable.

# In[17]:


a=12
b=24

b=a+b[InternetShortcut]
URL=http://localhost:8888/notebooks/ML_AI/Day3.ipynb#

a=b-a
b= b-a
print(b)
print(a)


# Question 5: Write a program to convert fahrenheit to kelvin and celsius both
# relation
# C=(F−32)×(5/9)
# Celsius (°C) = (Fahrenheit - 32) / 1.8
# Kelvin (K) = (Fahrenheit - 32) / 1.8 + 273.15
# 

# In[19]:


temp_farheit =int(input())

temp_cel= (temp_farheit-32)/1.8
print(temp_cel)
temp_keln= ((temp_farheit - 32) / 1.8) + 273.15
print(temp_keln)


# Question 6: Write a program to demonstrate all the available data types in Python. Hint: Use type() function.

# In[22]:


a= 5
b= 4.5
c= "data"
print(type(a))
print(type(b))
print(type(c))


# In[ ]:




