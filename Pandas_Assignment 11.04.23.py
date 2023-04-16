#!/usr/bin/env python
# coding: utf-8

# ![logo.png](attachment:logo.png)

# # PANDAS ASSIGNMENT

# In[2]:


import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings("ignore") 


# ## After reading the dataset, assign it named "df"

# In[6]:


df = pd.read_csv("data.csv", encoding="unicode_escape")
df


# ![image.png](attachment:image.png)

# ## Check the Head of the DataFrame

# In[8]:


df.head(7)


# ![image.png](attachment:image.png)

# ## Find out the describe and info attributes of the dataframe

# In[9]:


df.info()


# ![image.png](attachment:image.png)

# In[ ]:





# ![image.png](attachment:image.png)

# ## Find out the shape and size info of the dataset

# In[10]:


df.describe(include = "all").T


# ![image.png](attachment:image.png)

# ![image.png](attachment:image.png)

# ## Find out the types values of the columns

# In[11]:


df.shape


# In[12]:


df.size


# ![image.png](attachment:image.png)

# ## Find out the non-null counts of the columns

# In[13]:


types = df.dtypes
types


# In[14]:


df.dtypes
nonnull = df.notnull().sum().sort_values(ascending=False)

print(nonnull)


# ![image.png](attachment:image.png)

# ## Find out the null counts of the columns

# In[15]:


n_count = df.notnull().sum().sort_values(ascending=False)
print(n_count)


# ![image.png](attachment:image.png)

# ## Find out the unique counts of the columns

# In[16]:


u_count = df.nunique().sort_values(ascending = False)
print(u_count)


# ![image.png](attachment:image.png)

# ## Combine the dataframes you created in questions 5-6-7-8

# In[17]:


a = [types, nonnull, n_count, u_count]

b = pd.concat(a, axis = 1)

columns = ["dtype, nonnull", "n_count", "u_count"]

b


# ![image.png](attachment:image.png)

# ## Uppercase all column names

# In[18]:


df1 = df.copy()
df1.columns = df.columns.str.upper()
df1.head()


# ![image.png](attachment:image.png)

# ## What is the average of Product sold and the average price of Product per unit?

# In[19]:


df.head()
df.columns = df.columns.str.title()


# In[20]:


df


# In[21]:


df[["Unitprice", "Quantity"]].mean()


# ![image.png](attachment:image.png)

# ## What are the highest and lowest purchase prices?

# In[22]:


print(df["Unitprice"].max())


# In[23]:


print(df["Unitprice"].min())


# ![image.png](attachment:image.png)

# ## List the country names and number of their records belongs to each country

# In[24]:


df.Country.value_counts()


# ![image.png](attachment:image.png)

# ## How many records are there in the Germany?

# In[25]:


df[df["Country"] == "Germany"].count()


# ![image.png](attachment:image.png)

# ## Create a column named "Total" which shows the total amount of spend using UnitPrice and Quantity

# In[26]:


df["Total"] = df["Unitprice"] * df["Quantity"]

df.head()


# ![image.png](attachment:image.png)

# ## Show total spending amount according to the Countries and their percentages.

# In[27]:


df.groupby("Country")["Total"].sum().sort_values()


# ![image.png](attachment:image.png)

# In[ ]:





# ![image.png](attachment:image.png)

# ## Which Country spend least?

# In[28]:


df.groupby("Country").Total.sum().nsmallest(1)


# ![image.png](attachment:image.png)

# ## Which Country spend most?

# In[29]:


df.groupby("Country").Total.sum().nlargest(1)


# ![image.png](attachment:image.png)

# ## Calculate the average of spending according to country with apply function and create a new feature named "Average_Spend"

# In[30]:


df.groupby("Country").Total.apply(np.mean)


# ![image.png](attachment:image.png)

# In[32]:


df["Average_Spend"] = df.groupby("Country").Total.transform("mean")
df.sample(5)


# ![image.png](attachment:image.png)

# ## Calculate average, min, max of spending according to country with agg() function and create new features named "Max_Spend" and "Min_Spend"

# In[43]:


df.groupby("Country").Total.agg(["min","mean","max"])


# ![image.png](attachment:image.png)

# In[35]:


df["Max_Spend"] = df.groupby("Country").Total.transform("max")
df["Min_Spend"] = df.groupby("Country").Total.transform("min")
df.head()


# ![image.png](attachment:image.png)

# ## What is the max Total spending in whole dataset and show all records of that spending?

# In[36]:


df[df.Total == df.Total.max()]


# ![image.png](attachment:image.png)

# ## How many people who live in France spend more than average Total?

# In[37]:


df[(df.Total > df.Total.mean()) & (df.Country == "France")].count()


# ![image.png](attachment:image.png)

# ## Convert datatype of "InvoiceDate" to datetime and assign it to new column name "InvoiceDate2"

# In[68]:


df


# In[69]:


df["Invoicedate2"] = pd.to_datetime(df.Invoicedate)

df.info()


# ![image.png](attachment:image.png)

# ## Take only date values (year-month-day) from InvoiceDate2 and assign it to a new column named date

# In[72]:


df["date"] =  df["Invoicedate2"].dt.to_period("D")

df.head()


# ![image.png](attachment:image.png)

# ## Drop "InvoiceDate2" and "InvoiceDate" columns permanently

# In[73]:


df.drop(["Invoicedate2", "Invoicedate"], axis=1, inplace=True)

df.head()


# ![image.png](attachment:image.png)

# ## Remove A, B, G and E characters at the first 5 rows of "StockCode" in ecom dataframe with a string method

# In[75]:


df["Stockcode"].str.replace("[A, B, G, E]", "").head()


# ![image.png](attachment:image.png)

# ## Take only "Total" and "date" columns with loc and craete a new df named df2

# In[80]:


df2 = df.loc[: , ["Total", "date"]]

df2


# ![image.png](attachment:image.png)

# ## Take only "InvoiceNo" and "CustomerID" columns with iloc and craete a new df named df3

# In[83]:


df3 = df.iloc[: , [0,5,7]]
df3


# ![image.png](attachment:image.png)

# ## Combine "df2" and "df3" with concat() method

# In[84]:


pd.concat([df2, df3], axis = 1)


# ![image.png](attachment:image.png)

# ## Combine "df2" and "df3" with join() method

# In[85]:


df2.join(df3, lsuffix = "_left", rsuffix = "_right")


# ![image.png](attachment:image.png)

# ![logo.png](attachment:logo.png)
