
# coding: utf-8

# In[17]:


import math
import numpy as np
def quadratic(a, b, c):
    discriminant = b**2-4*a*c
    if discriminant < 0:
        message = "no real roots"
        root1 = np.nan
        root2 = np.nan
    else:
        message = 'real roots'
        root1 = (-b + math.sqrt(discriminant))/2/a
        root2 = (-b - math.sqrt(discriminant))/2/a
    return(root1, root2, message)


# In[18]:


a,b,c = 1,4,4


# In[21]:


root1, root2, message = quadratic(a, b, c)
print(message, root1, root2)


# In[22]:


print(quadratic(2,3,4))

