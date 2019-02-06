
# coding: utf-8

# In[280]:


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


# In[178]:


mydataset = "Documents\\patients.csv"
patients = pd.read_csv(mydataset)



# In[179]:


patients.head()


# In[165]:


patients.shape


# In[180]:


patients.loc[:, ['Age', 'Gender', 'Height', 'Weight', 'Smoker', 'Location', 'SelfAssessedHealthStatus']]


# In[284]:


sb.pairplot(patients)


# In[286]:


lm = smapi.ols(formula = "Systolic~Age+Gender+Height+Weight+Smoker+Location+SelfAssessedHealthStatus", data=df).fit()
lm.summary()


# In[287]:


fig, ax = plt.subplots(figsize=(100,7))
fig = sm.graphics.influence_plot(lm, ax=ax, criterion="cooks")

