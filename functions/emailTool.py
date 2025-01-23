def SendEmail (data):

   from email.mime.text import MIMEText
   from email.mime.application import MIMEApplication
   from email.mime.multipart import MIMEMultipart
   from smtplib import SMTP
   import datetime, smtplib

   # import keyring
   # from pretty_html_table import build_table

   
   if __name__ == '__main__':
      import sys
      sys.path.append('/Users/ed/CodingOnMac/StockAnalysis/CreateStockLists/')

      from ignore import settings
      username = settings.username
      password = settings.password
      recipient = settings.recipient
   else:
      from ignore.settings import username
      from ignore.settings import password
      from ignore.settings import recipient

   try:
    
      message = MIMEMultipart()

      message['Subject'] = 'Stock List Query'
      message_content = data
      #message_content = build_table(data, 'blue_light')
      
      message.attach(MIMEText(message_content, 'html'))
      
      # service_id = 'Gmail'
      # password = keyring.get_password(service_id, sender) # Only working with Anaconda
         
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.ehlo()
      server.starttls()
      server.login(username, password)
      server.sendmail(username,recipient,message.as_string())
      server.quit()
   
   except Exception as e:
      print(f'Function SendEmail Failed: {e}')
      data.to_csv('ignore/results.csv', index=False)
    
   return()


if __name__ == '__main__':
  
  import os
  import pandas as pd

  #df = pd.read_csv(os.getcwd() + '/ignore/employees.csv') # Not clear why /functions isn't part of filepath

  SendEmail('hello world')

