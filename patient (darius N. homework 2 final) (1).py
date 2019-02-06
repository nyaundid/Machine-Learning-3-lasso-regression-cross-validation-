
# coding: utf-8

# In[28]:


import matplotlib as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import scale
import pandas as pd
from pylab import rcParams
import seaborn as sb
from collections import Counter
import statsmodels.formula.api as smapi
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols
import statsmodels.api as sm
from zipfile import*
def main(): 
    file_name = "patients_homework2"
    ZipFile(file_name, "w")


# In[23]:


mydataset = "Documents\\patients.csv"
patients = pd.read_csv(mydataset)



# In[8]:


patients.head()


# In[9]:


patients.shape


# In[10]:


patients.loc[:, ['Age', 'Gender', 'Height', 'Weight', 'Smoker', 'Location', 'SelfAssessedHealthStatus']]


# In[11]:


sb.pairplot(patients)


# In[15]:


df = pd.read_csv("Documents\\patients.csv",sep=",")


# In[16]:


lm = smapi.ols(formula = "Systolic~Age+Gender+Height+Weight+Smoker+Location+SelfAssessedHealthStatus", data=df).fit()
lm.summary()


# In[29]:


fig, ax = plt.subplots(figsize=(100,7))
fig = sm.graphics.influence_plot(lm, ax=ax, criterion="cooks")

