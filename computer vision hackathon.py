#!/usr/bin/env python
# coding: utf-8

# In[78]:


import numpy as np
import cv2


# In[102]:


good_image = 'C:\\Users\\Ritzzz\\Downloads\good.png'
test_image = 'C:\\Users\\Ritzzz\\Downloads\Flash1.png'
image = cv2.imread(good_image)


# In[103]:


import numpy as np
from PIL import Image

g_image = Image.open(good_image)

if g_image.mode != "L":
    g_image =g_image.convert("L")


g_matrix = np.array(g_image)


print(g_matrix)


# In[104]:


t_image = Image.open(test_image)
if t_image.mode != "L":
    t_image =t_image.convert("L")
t_matrix = np.array(t_image)  
print(t_matrix)


# In[105]:


diff_matrix = g_matrix-t_matrix
print(diff_matrix)
cut_result = np.any(diff_matrix > 0)
flash_result = np.any(diff_matrix < 0)

if cut_result:
    print("The image is Cut")
elif flash_result:
    print("The image is flash")
else:
    print("It is a good image")


# In[ ]:





# In[ ]:




