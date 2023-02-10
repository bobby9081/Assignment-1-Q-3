#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Write a Python program to count the number of even and odd numbers from a series of numbers.


# In[5]:


a = [1,2,3,4,5,6,7,8,9]
b=0
c=0
for num in a:
    
    if num % 2 == 0:
        b += 1
 
    else:
        c += 1
 
print("Even numbers in the list: ", b)
print("Odd numbers in the list: ", c)

