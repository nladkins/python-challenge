#!/usr/bin/env python
# coding: utf-8

# In[1]:


#dependencies
import os
import csv
import pandas as pd


# In[2]:


# Store filepath in a variable
data_file = "Resources/budget_data.csv"


# In[3]:


# Read the Data file with the pandas library, but enconding just in case.
data_file = os.path.join("Resources", "budget_data.csv")


# In[4]:


# create a list
changes = []

# for row 1, change needs to be zero as you can't subtract from header.
change = 0 
with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        difference = int(row[1]) - change
        change = int(row[1])
        changes.append(difference)
changes

#Remove initial profit loss value from new list
first_pl = changes.pop(0)


# In[5]:


# average of the changes
avg_change = round(sum(changes)/len(changes), 2)


# In[6]:


# Use Pandas to read data (pd = Pandas) and the "head" method.
data_file_df = pd.read_csv(data_file)


# In[7]:


# Use Pandas to read list (pd = Pandas).
df_list = pd.read_csv(data_file)


# In[8]:


# Review headers
data_file_df.head(20)


# In[9]:


months = data_file_df["Date"].count()
profit = data_file_df["Profit/Losses"].sum()
greatest_increase = max(changes)
lowest_increase = min(changes)
print("FINANCIAL ANALYSIS")
print("-----------------------------------------")
print("Total Months ", "=", months)
print("Total Profit ", "= $", profit)
print("Average Monthly Change ", "= $", avg_change)
print("Greatest Increase ", "= $", greatest_increase)
print("Greatest Decrease", "= $", lowest_increase)


# In[10]:


# my attempt to output to txt failed, so I saved text results manually.
# with open(os.path.join('Analysis.txt'),'w') as outfile:
#     data_file_df.to_string(outfile)

