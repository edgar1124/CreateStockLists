#!/usr/bin/env python
# coding: utf-8

# In[6]:


#######################################################################################################
# Stock Market Analysis                                                                               #
#                                                                                                     #
# This code creates a list of all active stock tickers traded on US stock exchanges and saves the     #   
# data to a csv file.                                                                                 #
#                                                                                                     #
# The code uses the following naming convention: variable_names, FunctionNames, fileNames.            #
#                                                                                                     #
# by Edgar Fogelman                                                                                   #
#                                                                                                     #
#######################################################################################################


# In[7]:


import csv, datetime, logging, os, pickle
import pandas as pd
from polygon import RESTClient
from time import sleep

from functions import exchangeData, loggingFile, readData, saveData
from ignore import settings
key = settings.key


# In[9]:


# Set variable and file path for use in testing or deployment
#filePath.SetFilePath()

# Set filename and filepaths for logs, and delete old log files every Sunday
#filename_logs, filepath_logs = loggingFile.ConfigureLoggingFile('/logs/WikipediaStockSearch_log.txt')

##############

logging.basicConfig(filename = loggingFile.ConfigureLoggingFile('CreateStockLists_Log.txt') +                     '/CreateStockLists_Log.txt', level = logging.DEBUG,                     format = '%(asctime)s - %(levelname)s - %(message)s')

logging.info('Logging configured')


# In[4]:



exchange_list, client_RESTClient = exchangeData.GetData()
saveData.WriteToPickle('activeStockExchanges', exchange_list)

logging.info(f'Active US stock exchange data acquired, cleaned, and saved')


# In[5]:


active_tickers = []

for ex in exchange_list:
    i = 0
    print(ex)

    for t in client_RESTClient.list_tickers(market='stocks', exchange = ex):
        active_tickers.append(t.ticker)
        i+=1
        sleep(20)

    #file_name = ex + i
    #saveData.WriteToPickle(file_name)
    print(f'i: {i}')


# In[48]:


saveData.WriteToPickle('stockList', active_tickers)


# In[ ]:




