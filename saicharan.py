#!/usr/bin/env python
# coding: utf-8

# In[7]:


#importing libraries
import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# 
# 
# # Read the dataset

# In[8]:


#importing dataset
data = pd.read_csv('E:\python\pubg.csv')
print(data)
data.head()


# # Check the datatype of all the columns.

# In[10]:


#checking datatypes
data.dtypes


# # Find the summary of all the numerical columns and write your findings about it.

# In[11]:


#summarising the numerical data using describe function
data.describe()


# # The average person kills how many players

# In[18]:


avg = data['kills'].mean()
print( 'the average person kills:',avg,'players')


# # 99% of people have how many kills

# In[25]:


np.percentile(data.kills,99)


# # The most kills ever recorded are how much

# In[19]:


most_kills = data['kills'].max()
print('most kills recorded are:', most_kills)


# # Print all the columns of the dataframe

# In[20]:


data.columns


# # Comment on distribution of the match's duration. Use seaborn

# In[24]:


print(data['matchDuration'])


# 

# In[ ]:





# # Comment on distribution of the walk distance

# In[37]:


sns.distplot(data.walkDistance);


# # Plot distribution of the match's duration vs walk distance 

# In[39]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use("classic")
plt.figure()

# ploting for match duration
plt.subplot(2,1,1)
plt.plot(data["matchDuration"], "-")
plt.xlabel("Match Duration");

# ploting for walk duration
plt.subplot(2,1,2)
plt.plot(data["walkDistance"], "--")
plt.xlabel("Walk Distance");


# # Plot distribution of the match's duration vs walk distance side by side

# In[43]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use("classic")
plt.figure(figsize=(8,4))

# ploting for match duration
plt.subplot(1,2,1)
plt.plot(data["matchDuration"], "-")
plt.xlabel("Match Duration");

# ploting for walk duration
plt.subplot(1,2,2)
plt.plot(data["walkDistance"], "--")
plt.xlabel("Walk Distance");


# # Pairplot the dataframe. Comment on kills vs damage dealt, Comment on maxPlace vs numGroups

# In[45]:


sns.pairplot(data.head(700));


# # How many unique values are there in 'matchType' and what are their counts

# In[46]:


unique_values=pd.unique(data['matchType'])
print('unique values are:',unique_values)
count=len(unique_values)
print('counts:',count)


# # Plot a barplot of ‘matchType’ vs 'killPoints'.

# In[86]:


sns.boxplot(x='matchType',y='killPoints',data=data)
plt.xticks(rotation=80)


# # Plot a barplot of ‘matchType’ vs ‘weaponsAcquired’

# In[85]:


sns.boxplot(x='matchType',y='weaponsAcquired',data=data)
plt.xticks(rotation=80)


# # Find the Categorical columns.

# In[82]:


data.select_dtypes(exclude=['number','bool'])


# # Plot a boxplot of ‘matchType’ vs ‘winPlacePerc’.

# In[84]:


sns.boxplot(x='matchType',y='winPlacePerc',data=data)
plt.xticks(rotation=80)


# # Plot a boxplot of ‘matchType’ vs ‘matchDuration’.

# In[87]:


sns.boxplot(x='matchType',y='matchDuration',data=data)
plt.xticks(rotation=80)


# # Change the orientation of the above plot to horizontal.

# In[89]:


sns.boxplot( x='matchDuration', y='matchType',data=data);


# # Add a new column called ‘KILL’ which contains the sum of following columns viz. headshotKills,teamKills, roadKills.

# In[91]:


data['kill']=data.headshotKills+data.roadKills+data.teamKills
data['kill']


# # Round off column ‘winPlacePerc’ to 2 decimals.

# In[96]:


data['winPlacePerc'].round(2)


# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




