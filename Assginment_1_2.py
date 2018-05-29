
# coding: utf-8

# Welcome to your assignment on Pandas and Matplotlib!
# In case you face any difficulty or you have any doubts related to this assignment, or Pandas or Matplotlib in general, do not hesitate to ask on the Slack channel.

# # Importing Libraries
# 
# We shall start by importing the Python libraries you will need to run the code.

# In[5]:


import pandas as pd
from matplotlib import pyplot as plt
import matplotlib

get_ipython().run_line_magic('matplotlib', 'inline')


# # Importing the Data
# 
# Import the data stored in "day.csv" using Pandas and store it in a DataFrame named df.
# Also, since the data contains many columns that you may find unnecessary, you may drop them off.

# In[10]:


#Fill in the incomplete code here
df = pd.read_csv("day.csv")

drop_list = ['instant', 'season', 'yr']


df.drop(drop_list,axis=1,inplace=True)


# # Plotting the data
# 
# With the data stored in our Pandas dataframe, we are now ready to plot the data to gain some insights on the data.
# We will define functions for each plot to make our code re-usable.

# But before plotting, you must set some parameters common to all the plots. This is done in order to make the visibility and readability of the plots better. This can be done by changing the default rc settings defined in the matplotlibrc configuration files. One example is given.

# In[24]:


#Set plot size to 14" x 7" (Solved Exapmle)
matplotlib.rc('figure', figsize = (14, 7))

#Set the font size to 15
font={'size':15}


# ## Scatter Plot
# 
# This is the most used plot for gaing insight into data while dealing with Machine Learning problems. For your convenience, the code for scatter plot is given as an exapmle.

# In[ ]:


def scatter_plot(x_data, y_data, x_label, y_label, title):
    
    fig, ax = plt.subplots()
    ax.scatter(x_data, y_data, s = 30, color = '#539caf', alpha = 0.75)
    
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    
scatter_plot(x_data = df['temp']
            , y_data = df['cnt']
            , x_label = 'Normalized temperature (C)'
            , y_label = 'Check outs'
            , title = 'Number of Check Outs vs Temperature')


# # Histogram

# In[38]:


#Fill the function given below
def histogram(data, x_label, y_label, title):
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.hist(data,rwidth=0.95,color='orange');
    
    
histogram( df['registered']
           , 'Check outs'
           , 'Frequency'
           ,  'Distribution of Registered Check Outs')    


# # Line Plot

# In[41]:


#Fill the function given below
def lineplot(x_data, y_data, x_label, y_label, title):
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.plot(x_data,y_data)
    

    
    
#Calling the function to create plot
lineplot(x_data = df['dteday']
         , y_data = df['cnt']
         , x_label = 'Date'
         , y_label = 'Total Checkouts'
         , title = 'Total Checkouts for Each Day')


# # Comparing Two Line Plots
# 
# This is useful for comparing two variables over a third variable. It must be noted that these variables may have different scales (they do in the example given below).

# In[43]:


#Fill the function given below
def lineplot2y(x_data, x_label, y1_data, y1_label, y2_data, y2_label, title):
    plt.subplot(1,2,1)
    plt.plot(x_data,y1_data)
    plt.xlabel(x_label)
    plt.ylabel(y1_label)
    plt.title(title)
    
    plt.subplot(1,2,2)
    plt.plot(x_data,y2_data)
    plt.xlabel(x_label)
    plt.ylabel(y2_label)
    plt.title(title)
    


#Calling the function to create plot
lineplot2y(x_data = df['dteday']
           , x_label = 'Date'
           , y1_data = df['casual']
           , y1_label = 'Casual Checkouts'
           , y2_data = df['registered']
           , y2_label = 'Registered Checkouts'
           , title = 'No. of Registered vs Casual Checkouts for Each Day')


# # And You're Done!
# 
# Congratulations on completing the second part of your first assignment. There are lots of plots you can explore and try on the numerous fields given in "day.csv". You can also do numpy operations on the data to derive more meaningful insights if you wish to.

# You need to submit this Python notebook for this part of the assignment.
