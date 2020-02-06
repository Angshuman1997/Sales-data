#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
df=pd.read_csv("C:\\Users\\Angshuman Bardhan\\Desktop\\Data Set\SALES.csv")
df


# In[45]:


df['DATE']


# In[52]:


d1=df.groupby(['CITY','DATE'])['SALES'].sum()
d1


# In[7]:


d2=df.groupby(['DATE','CITY'])['CUSTOMER_COUNT'].sum()
d2


# In[17]:


d3=df.groupby(['CITY'])['CUSTOMER_COUNT'].sum()
d3


# In[18]:


d4=df.groupby(['CITY'])['SALES'].sum()
d4


# In[19]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels =['Bangalore','Chennai','Pune']
sizes = d4

explode = (0,0,0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True,
         startangle=60)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


# In[20]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels =['Bangalore','Chennai','Pune']
sizes = d3

explode = (0,0,0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True,
         startangle=60)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


# In[ ]:




