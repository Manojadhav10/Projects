#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


Emp = pd.read_csv('employees.csv')


# In[3]:


Emp.head()


# In[4]:


Emp.info()


# In[5]:


# Find the null value
Emp.isnull().sum()


# In[6]:


# Check duplicates value()
Emp[Emp.duplicated()]


# In[7]:


Emp.drop_duplicates()


# In[8]:


Emp.shape


# In[9]:


# To check the correlation matrix among the columns
# Correlation -  Relationship of one column with other columns
# positive correlation - Relationship between two columns are moving in the same direction directly proportional
# Negative correlation -  Inversely proportional 
# Zero correlation - There is no existing relationship between the two columns
#  -1 to 1  
Emp.corr()


# In[10]:


# Data visualization analysing different fetures


# In[11]:


a = ['dept','numberOfProjects','timeSpent.company','workAccident','promotionInLast5years','salary']


# In[12]:


a


# In[13]:


# enumerate function is use extracting the data as wll the index values of data i= indexvalue , J =data

fig = plt.subplots(figsize = (10,20))
    
for i,j in enumerate(a):
    plt.subplot(3,2,i+1)
    plt.subplots_adjust(hspace = 0.4)
    plt.grid(True)
    plt.xticks(rotation = 90)
    sns.countplot(x = j,data = Emp , hue = 'left') #hue for categorical data
plt.show()


# In[14]:


# # Conclusion
# Dept -> Most of the employees that are leaving are from sales, technical and support department.
# No. of Projects -> Pepole with lowest as well highest no. of projects have a higher chance of leaving the company.
# Time spent -> Employees after spending 3-5 years with the company are leaving the most.
# Work Accident -> This does not effect the employees decision for leaving the company at all.
# Promotion -> All the employees who are leaving have not been promoted in last 5 years.
# Salary -> Employees who are leaving, are not happy with the salary that they are getting, 
#             They feel like they are getting very less salary.

