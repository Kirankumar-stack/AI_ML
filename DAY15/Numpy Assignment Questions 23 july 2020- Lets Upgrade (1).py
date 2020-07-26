#!/usr/bin/env python
# coding: utf-8

# # 1. Create a 3x3x3 array with random values 

# In[1]:


import numpy as np
ran_data = np.random.randint(1,90,(3,3)) 
print(ran_data)


# # 2.Create a 5x5 matrix with values 1,2,3,4 just below the diagonal

# In[15]:


import numpy as np
x = np.diag([1, 2, 3, 4, 5])
print(x)
y = np.diag(1+np.arange(4))
print( y)
z = np.diag(1+np.arange(4),k=-1)
print( z)


# # 3.Create a 8x8 matrix and fill it with a checkerboard pattern

# In[19]:


import numpy as np
x = np.ones((3,3))
print("Checkerboard pattern:")
x = np.zeros((8,8),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)


# # 4. Normalize a 5x5 random matrix

# In[24]:


import numpy as np
x= np.random.random((3,3))
print("Original Array:")
print(x)
print("max,min munbers:", xmax, xmin )
xmax, xmin = x.max(), x.min()
x = (x - xmin)/(xmax - xmin)
print("After normalization:")
print(x)


# # 5.  How to find common values between two arrays?

# In[25]:


import numpy as np
array1 = np.array([0, 10, 20, 40, 60])
print("Array1: ",array1)
array2 = [10, 30, 40]
print("Array2: ",array2)
print("Common values between two arrays:")
print(np.intersect1d(array1, array2))


# # 6.How to get the dates of yesterday, today and tomorrow?

# In[26]:


import numpy as np
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
print("Yestraday: ",yesterday)
today     = np.datetime64('today', 'D')
print("Today: ",today)
tomorrow  = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("Tomorrow: ",tomorrow)


# # 7. Consider two random array A and B, check if they are equal

# In[28]:


import numpy as np
x = np.random.randint(0,5,6)
print("First array:")
print(x)
y = np.random.randint(0,5,6)
print("Second array:")
print(y)
print("Test above two arrays are equal or not!")
array_equal = np.allclose(x, y)
print(array_equal)


# # 8.Create random vector of size 10 and replace the maximum value by 0 

# In[33]:


import numpy as np
x = np.random.random(10)
print("Original array:")
print(x)
x[x.argmax()] = 0
print("Maximum value replaced by 0:")
print(x)


# # 9. How to print all the values of an array?

# In[ ]:





# # 10.Subtract the mean of each row of a matrix

# In[34]:


import numpy as np
print("Original matrix:\n")
X = np.random.rand(5, 10)
print(X)
print("\nSubtract the mean of each row of the said matrix:\n")
Y = X - X.mean(axis=1, keepdims=True)
print(Y)


# # 11.Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)? 

# In[46]:


Z = np.ones(10)

I = np.random.randint(0,len(Z),20)

Z += np.bincount(I, minlength=len(Z))

print(Z)


# In[47]:


# Another solution

# Author: Bartosz Telenczuk

np.add.at(Z, I, 1)

print(Z)


# # 12.How to get the diagonal of a dot product?

# In[45]:


# We need install numpy in order to import it 
import numpy as np 

# input two matrices 
mat1 = ([1, 6, 5],[3 ,4, 8],[2, 12, 3]) 
mat2 = ([3, 4, 6],[5, 6, 7],[6,56, 7]) 

# This will return dot product 
res = np.dot(mat1,mat2) 


# print resulted matrix 
print(res) 


# # 13.How to find the most frequent value in an array?

# In[44]:


import numpy as np
x = np.random.randint(0, 10, 40)
print("Original array:")
print(x)
print("Most frequent value in the above array:")
print(np.bincount(x).argmax())


# # 14.How to get the n largest values of an array

# In[41]:


import numpy as np
x = np.arange(10)
print("Original array:")
print(x)
np.random.shuffle(x)
n = 1
print (x[np.argsort(x)[-n:]])


# # 15.How to create a record array from a regular array?

# In[37]:


import numpy as np
a1=np.array([1,2,3,4])
a2=np.array(['Red','Green','White','Orange'])
a3=np.array([12.20,15,20,40])
result= np.core.records.fromarrays([a1, a2, a3],names='a,b,c')
print(result[0])
print(result[1])
print(result[2])


# In[ ]:




