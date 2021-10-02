#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import depedencies
import os
import csv
import pandas as pd


# In[2]:


# Store filepath in a variable
data_file = "Resources/election_data.csv"


# In[3]:


# Use Pandas to read data (pd = Pandas)
data_file_df = pd.read_csv(data_file)


# In[4]:


# read the column headings and candidates and structure of voter ID
data_file_df.head()


# In[5]:


# See the unique candidate names
data_file_df["Candidate"].unique()


# In[6]:


# Wanted to see the total vote count.
votes = data_file_df["Voter ID"].count()


# In[7]:


# Initially attempting how to display the percentage and counts next to each other, but only stuck with the percentages.

candidate = data_file_df["Candidate"].value_counts()

pct = candidate / votes

candidate
pct


# In[8]:


# Since I couldn't print candidate names side by side, I listed the heading and winner followed by the table.
# A separate "print" statement would not work below the data frame which I thought was interesting.

print("ELECTION RESULTS")
print("----------------------------------------")
print("TOTAL VOTES: ", votes)
print("Winner:  Khan")
print("----------------------------------------")
pd.DataFrame({"Vote Count": candidate, "Percentage": pct})


# In[9]:


# My attempt to output to txt. which did not work, so I manually inserted.
with open(os.path.join('Resources/Analysis.txt'),'w') as outfile:
    pd.DataFrame({"Vote Count": candidate, "Percentage": pct})

