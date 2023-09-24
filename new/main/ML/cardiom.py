#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder as le

import seaborn as sns


# In[3]:


df=pd.read_csv(r"C:\Users\sanjay\project\env\new\main\ML\cardio.csv")
df=df[ df[ "EF" ].str.contains( "EMPTY" )==False ]
df['EF'] = df['EF'].astype(float)
df=df[ df[ "CREATININE" ].str.contains( "EMPTY" )==False ]
df['CREATININE'] = df['CREATININE'].astype(float)
df=df[ df[ "BNP" ].str.contains( "EMPTY" )==False ]
df['BNP'] = df['BNP'].astype(float)
df=df[ df[ "UREA" ].str.contains( "EMPTY" )==False ]
df['UREA'] = df['UREA'].astype(float)
df=df[ df[ "GLUCOSE" ].str.contains( "EMPTY" )==False ]
df['GLUCOSE'] = df['GLUCOSE'].astype(float)
df=df[ df[ "PLATELETS" ].str.contains( "EMPTY" )==False ]
df['PLATELETS'] = df['PLATELETS'].astype(float)

df['GENDER']= le().fit_transform(df['GENDER'])
df.dropna(inplace=True)
df


# In[4]:


X=df.drop(['SNO', 'MRD No.', 'D.O.A', 'D.O.D', 'RURAL','TYPE OF ADMISSION-EMERGENCY/OPD', 'month year', 'DURATION OF STAY',
       'duration of intensive unit stay', 'OUTCOME','DM','CKD', 'HB', 'TLC','SEVERE ANAEMIA', 'ANAEMIA', 'STABLE ANGINA', 'ACS', 'STEMI',
        'HFREF', 'HFNEF', 'VALVULAR',
       'CHB', 'SSS', 'AKI', 'CVA INFRACT', 'CVA BLEED', 'VT', 'PSVT',
       'CONGENITAL', 'UTI', 'NEURO CARDIOGENIC SYNCOPE', 'ORTHOSTATIC',
       'INFECTIVE ENDOCARDITIS', 'DVT', 'CARDIOGENIC SHOCK', 'SHOCK',
       'PULMONARY EMBOLISM', 'CHEST INFECTION',"PRIOR CMP"],axis="columns")
X


# In[5]:


y=df["PRIOR CMP"]
y


# In[6]:


X["GENDER"].unique()
X["CREATININE"].unique()


# In[7]:


X.corr()
sns.heatmap(data=X.corr(),annot=True,cmap='viridis')


# In[8]:


X=X.drop("EF",axis=1)


# In[9]:


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# In[69]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01, random_state=101)


# In[70]:


scaler = StandardScaler()
scaled_X_train = scaler.fit_transform(X_train)
scaled_X_test = scaler.transform(X_test)


# In[71]:


from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score as ac


# In[72]:


log_model = LogisticRegression()


# In[73]:


log_model.fit(scaled_X_train,y_train)


# In[74]:


from sklearn.metrics import classification_report


# In[76]:


y_pred = log_model.predict(scaled_X_test)
print(classification_report(y_test,y_pred))
def acc():
       return ac(y_test,y_pred)


# In[61]:




