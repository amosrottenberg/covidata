#!/usr/bin/env python
# coding: utf-8

# #### get all data

# In[75]:


import pandas as pd
import os
import glob
PATH = r'C:\start\עמוס\git\nCoV2019\dataset_archive'
os.chdir(PATH)
paths = glob.glob('*outside*')
print(paths)
dfs = []
for path in paths:
    try:
        dfs.append(pd.read_csv(path))
    except UnicodeDecodeError:
        print('here')
        print(path)
# data = pd.read_csv('outside_Hubei.data.16032020T093212.csv')
# data
# data = data[['age', 'city', 'country', 'longitude', 'latitude', 'location', 'country_new']]
# data


# #### create new csv with relevant information

# In[82]:


big_frame = pd.concat(dfs, ignore_index=True)
CSV_PATH = r'C:\start\עמוס\git\analasis\data17032020.csv'
big_frame = big_frame[['city', 'country', 'country_new', 'longitude', 'latitude', 'date_onset_symptoms', 'date_admission_hospital', 'date_confirmation', 'symptoms']]
big_frame.to_csv(CSV_PATH, index=False)


# #### read the csv

# In[104]:


data = pd.read_csv(CSV_PATH)


# #### find symptoms

# In[105]:


symptoms = data[['symptoms']]
symptoms = symptoms[symptoms.symptoms.notnull()]
symptoms = symptoms.values.tolist()
symptoms


# #### split to list

# In[106]:


symptoms = [item[0].replace(';', ',') for item in symptoms]
symptoms
symptoms = [item.split(', ') for item in symptoms]
symptoms


# In[107]:


from functools import reduce
symptoms = list(reduce(lambda x, y: x+y , symptoms))
symptoms


# #### count the different symptoms

# In[111]:


import collections
symptoms_mifkad = collections.Counter(symptoms)
common_symptoms = symptoms_mifkad.most_common()
common_symptoms


# In[ ]:





# In[ ]:





# In[ ]:




