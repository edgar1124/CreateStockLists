import datetime, logging, os

def ConfigureLoggingFile (file_name):

  if 'Mac' in os.getcwd():
    file_path = os.path.dirname(__file__).replace('functions','ignore/logs')
  else:
    file_path = os.path.dirname(__file__).replace('CreateStockLists/functions','Logs')
  
  try:

    if not os.path.isdir(file_path):
      os.mkdir(file_path) # creates filepath for logs if one does not already exist
      
    if (datetime.datetime.today().weekday() == 6) and (file_name != 'Test'):
      # Prevents log file from becoming too big by deleting it on Saturdays
      os.remove(file_path + '/' + file_name)

  except Exception as e:
    print(f'ConfigureLoggingFile Function error while getting stock info: {e}')

  print(f'Logging filepath is {file_path}')

  return(file_path + '/' + file_name)

if __name__ == '__main__':
  print(ConfigureLoggingFile('Test'))