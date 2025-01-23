#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


import csv, datetime, logging, os, pickle
import pandas as pd
from polygon import RESTClient
from time import sleep

from functions import emailTool, exchangeData, loggingFile, readData, saveData
from ignore import settings
key = settings.key


# In[3]:


# Set variable and file path for use in testing or deployment
#filePath.SetFilePath()

# Set filename and filepaths for logs, and delete old log files every Sunday
#filename_logs, filepath_logs = loggingFile.ConfigureLoggingFile('/logs/WikipediaStockSearch_log.txt')

##############

#logging.basicConfig(filename = loggingFile.ConfigureLoggingFile('createStockLists_Log.txt') + \
#                    '/createStockLists_Log.txt', level = logging.DEBUG, \
#                    format = '%(asctime)s - %(levelname)s - %(message)s')

logging.basicConfig(filename = loggingFile.ConfigureLoggingFile('StockList_Log.txt'),
                    level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

logging.info('Logging configured')


# In[4]:



exchange_list, client_RESTClient = exchangeData.GetData()
saveData.WriteToPickle('activeStockExchanges', exchange_list)

logging.info(f'Active US stock exchange data acquired, cleaned, and saved')


# In[5]:


active_tickers = []
i = 0

exchange_today = exchange_list[datetime.datetime.today().day%4]

print('Let"s go go go!')
for t in client_RESTClient.list_tickers(market='stocks', exchange = exchange_today):
    logging.info(f'/\/\/\/\/\/\/\/\/\/\/Beginning to process: {t}/\/\/\/\/\/\/\/\/\/\/')
    
    try:
        active_tickers.append(t.ticker)
        logging.info(f'Exchange: {exchange_today}, ticker: {t.ticker}, counter: {i}')
        i+=1
        sleep(20)

        if i%100 == 0:
                    
            try:
                emailTool.SendEmail(f'Exchange: {exchange_today}, ticker: {t.ticker}, counter: {i}')
                
            except Exception as e:
                logging.info(f'/\/\/\/\/\/\/\/\/\/\/Main exception: {e}/\/\/\/\/\/\/\/\/\/\/')


    except Exception as e:
        logging.info(f'/\/\/\/\/\/\/\/\/\/\/Main exception: {e}/\/\/\/\/\/\/\/\/\/\/')


logging.info('/\/\/\/\/\/\/\/\/\/\/Stock list compiled/\/\/\/\/\/\/\/\/\/\/')
file_name = exchange_today + '_StockList_' + i
saveData.WriteToPickle(file_name, active_tickers)

