#!/usr/bin/env python
# coding: utf-8

# # Worldwide Natural Gas Reserve Data Analysis.
# 
# 

# In[102]:


import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
url = 'https://www.worldometers.info/gas/'
html = requests.get(url).content
df_list = pd.read_html(html)
Oil_dataset = df_list[-1]
print(Oil_dataset)
Oil_dataset.to_csv('my data.csv')


# In[103]:


Oil_dataset.columns


# In[104]:


Oil_dataset.head()


# In[105]:


Oil_dataset.tail()


# In[242]:


Oil_dataset.shape


# In[246]:


y = Oil_dataset["Gas Reserves (MMcf)"]


# In[247]:


#Let's analyze top 10 countries per Gas reserve 


# In[248]:


TopTen_GasReserve = y.head(10) 


# In[249]:


TopTen_GasReserve


# In[250]:


PercentShare = Oil_dataset["World Share"]


# In[251]:


PercentShare = x.head(10)


# In[252]:


PercentShare


# In[115]:


TopCountries = Oil_dataset["Country"]


# In[116]:


TopTenCountries = TopCountries.head(10)


# In[253]:


TopTenCountries


# ### Let's split the dataset into 2 different dataset for analysis.
#     1 . Countries Per their Gas reserve 
#     2. Countries pee their percentile Gas reserve

# In[254]:


CtryPerShare = pd.DataFrame(Oil_dataset.head(10), columns= ['Country', 'World Share'])
CtryPerShare


# In[256]:


CtryPerReserve = pd.DataFrame(Oil_dataset.head(10), columns= ['Country', 'Gas Reserves (MMcf)'])


# In[257]:


CtryPerReserve


# In[258]:


fig = plt.figure(figsize = (18,7))

chart = plt.bar(CtryPerReserve['Country'], CtryPerReserve["Gas Reserves (MMcf)"])


# In[259]:



 CtryPerShare


# In[260]:


CtryPerShare.dtypes


# In[261]:


#Since the World Share datatype is represented as an object(string), we need to convert it back into the numeric value.
s = CtryPerShare['World Share'].str.replace(r'%', r'').astype('float')/100
CtryPerShare['World Share']  = pd.to_numeric(CtryPerShare['World Share'], errors='coerce').fillna(s)


# In[262]:


CtryPerShare


# In[264]:


#Let's create a pie chart to represent this countries 

fig = plt.figure(figsize = (10, 7))
plt.pie(CtryPerShare['World Share'], labels = CtryPerShare["Country"], shadow = True)
plt.show()


# In[265]:


fig = plt.figure(figsize = (18,7))
chart = plt.bar(CtryPerShare['Country'], CtryPerShare["World Share"])


# In[266]:



name = CtryPerShare['Country']
price = CtryPerShare['World Share']

# Figure Size
fig, ax = plt.subplots(figsize =(16, 9))

# Horizontal Bar Plot
ax.barh(name, price)

#Remove axes splines
for s in ['top', 'bottom', 'left', 'right']:
   ax.spines[s].set_visible(False)

#Remove x, y Ticks
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')

# Add padding between axes and labels
ax.xaxis.set_tick_params(pad = 5)
ax.yaxis.set_tick_params(pad = 10)

#Add x, y gridlines
ax.grid(b = True, color ='grey',
       linestyle ='-.', linewidth = 0.5,
       alpha = 0.2)

# Show top values
ax.invert_yaxis()

# Add annotation to bars
for i in ax.patches:
   plt.text(i.get_width(), i.get_y()+0.5,
            str(round((i.get_width()), 2)),
            fontsize = 10, fontweight ='bold',
            color ='grey')


#Add Plot Title
ax.set_title('Top 10 Countries Per % Natural Gas Reseve ',
            loc ='left', )

# # # Add Text watermark
# fig.text(0.9, 0.15, 'Jeeteshgavande30', fontsize = 12,
#          color ='grey', ha ='right', va ='bottom',
#          alpha = 0.7)

# Show Plot
plt.show()



# In[ ]:




