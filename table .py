#!/usr/bin/env python
# coding: utf-8

# In[1]:


while True:
    x=input("enter your number or stop" ' ')
    if x=='stop':
        break
    for y in range(1,11):
        x1=int(x)
        z=x1*y
        print('{}*{}={}'.format(x1,y,z))


# In[ ]:




