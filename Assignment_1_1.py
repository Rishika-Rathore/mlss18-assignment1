
# coding: utf-8

# In[2]:


import pickle
import numpy as np


# In[5]:


# Code to load the array
with open('array.pickle', 'rb') as p:
    arr = pickle.load(p)
   # print(len(arr))


# Check that the size of the array (arr) is 1000. Please report if any discrepancy.

# ## Task 1: Resize the array to a (20x50) matrix

# In[18]:


## BEGIN CODE
arr=np.resize(arr,(20,50))
print(arr[0])

## END CODE


# ## Task 2: Find the transpose of this matrix

# In[24]:


## BEGIN CODE
arr2=arr.transpose()
#print(arr2)
## END CODE


# ## Task 3: Find the dot product of the matrices created in Tasks 1 & 2

# In[27]:


## BEGIN CODE
mul=np.dot(arr,arr2)
#print(mul)
## END CODE


# ## Task 4: Find the row-wise sum of the resulting matrix

# In[35]:


## BEGIN CODE
ressum=[]
for row in mul:
    total=0
    for i in row:
        total=total+i
    ressum.append(total)  
#print(ressum)    
    
## END CODE


# ## Task 5: Find the square root of all elements in the resulting matrix

# In[42]:


## BEGIN CODE
t=0
for i in ressum:
    ressum[t]=i**0.5
    t=t+1
print(ressum)    
## END CODE


# ## Task 6: Find the sine value of all elements in the resulting matrix

# In[53]:


## BEGIN CODE

t=np.sin(ressum)

## END CODE


# ## Create submission file

# ## Assign the name of the variable containing the final matrix to VARIABLE_NAME variable.
# 
# VARIABLE_NAME = t
# with open('submission.pickle', 'wb') as p:
#     pickle.dump(VARIABLE_NAME, p)
