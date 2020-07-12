#!/usr/bin/env python
# coding: utf-8

# Question 1 : Write a Python program to find the first 20 non-even prime natural numbers. 

# In[20]:


nums = range(1,20)
for i in nums:
    for k in range(2,i):
        if(i%k == 0):
            break
    else:
        print(i)
        


# Question 2 : Write a Python program to implement 15 functions of string. 

# In[86]:


k = "kirankumar"
r="123"
print(k.capitalize())
print(k.count("k"))
print(k.index("u"))
print(k.upper())
print(k.find("n"))
print(k.casefold())
print(k.title())
print(k.expandtabs())
print(k.encode())
print(k.join(r))
print(k.split("u"))
print(k.zfill(7))
print(k.replace(k,"kumarkiran"))
print(k.isalpha())
print(k.swapcase())
print(k.splitlines())


# Question 3: Write a Python program to check if the given string is a Palindrome or Anagram or None of them. Display the message accordingly to the user. 

# In[ ]:





# Question 4: Write a Python's user defined function that removes all the additional characters from the string and converts it finally to lower case using built-in lower(). eg: If the string is "Dr. Darshan Ingle @AI-ML Trainer", then the output be "drdarshaningleaimltrainer

# In[72]:


import re
j= "kiran kumar @Bangalore"

final = [re.sub(r"[^a-zA-Z0-9]+", '', k) for k in j.split("\n")]
print(final)


# In[70]:


import re
a = '''hello? there A-Z-R_T(,**), world, welcome to python.
this **should? the next line#followed- by@ an#other %million^ %%like $this.'''

for k in a.split("\n"):
    print(re.sub(r"[^a-zA-Z0-9]+", '', k))


# In[ ]:




