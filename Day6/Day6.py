#!/usr/bin/env python
# coding: utf-8

# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only. 

# In[59]:


def find_comany_name(a):
    count=0
    lower=0
    higher =0
    b=len(a)
    for elm in a:
        count+=1
        if(elm == "@"):
            lower=count
           # print(lower)
        elif(elm=='.'): 
            higher= count
           # print(higher)                   
    if((lower == 0) or (higher == 0)):
        a= "invalid "
        higher = len(a)
        
    print(a[lower:higher-1])
    
find_comany_name("mulavagilikiran@gmail.com")    


# Question 2: Write a program that accepts a comma-separated sequence of words as input and prints the words in a comma separated sequence after sorting them alphabetically.

# In[67]:


words = ["Geeks", "For", "Geeks"] 
  
# Sorting list of strings 
words.sort() 
  
print(words)


# In[72]:


data = set(input())
print(data)


# In[ ]:





# Question 3: Create your own Jupyter Notebook for Sets. Reference link: https://www.w3schools.com/python/python_sets.asp 

# In[71]:


thisset = {"apple", "banana", "cherry"}
print(thisset)


# In[73]:


thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset) 


# Question 4:  Given a list of n-1 numbers ranging from 1 to n, your task is to find the missing number. There are no duplicates

# In[119]:


dta = [2,1,4,6,15,3,7,8,11]
def missing_num(data):
    f = [*range(0,(max(data)+1),1)]
    for elm in data:
        f.remove(elm)
    print(f)
    
missing_num(dta)


# Question 5: With a given list L, write a program to print this list L after removing all duplicate values with original order reserved. 

# In[123]:


data1 = [1,2,4,1,6,7,8,2,4,0]
data1 = list( dict.fromkeys(data1) )
print(data1)


# In[ ]:




