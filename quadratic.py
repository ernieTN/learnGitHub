
# coding: utf-8

# In[9]:


import math
def quadratic(a, b, c):
    discriminant = b**2-4*a*c
    root1 = (-b + math.sqrt(discriminant))/2/a
    root2 = (-b - math.sqrt(discriminant))/2/a
    return(root1, root2)


# In[13]:


a,b,c = 1,4,4


# In[14]:


root1, root2 = quadratic(a, b, c)
print(root1)
print(root2)

