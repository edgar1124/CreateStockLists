import datetime, logging, os

def ConfigureLoggingFile (filename):

  if 'Mac' in os.getcwd():
    filepath = os.path.dirname(__file__).replace('functions','ignore/logs')
  else:
    filepath = os.path.dirname(__file__).replace('CreateStockLists/functions','Logs')
  
  try:

    if not os.path.isdir(filepath):
      os.mkdir(filepath) # creates filepath for logs if one does not already exist
      
    if (datetime.datetime.today().weekday() == 6) and (filename != 'Test'):
      # Prevents log file from becoming too big by deleting it on Saturdays
      os.remove(filepath + '/' + filename)

  except Exception as e:
    logging.info(f'/\/\/\/\/\/\/\/\/\/\/ConfigureLoggingFile Function error while getting stock info: {e}/\/\/\/\/\/\/\/\/\/\/')

  print(f'Logging filepath is {filepath}')

  return(filepath)

if __name__ == '__main__':
  print(ConfigureLoggingFile('Test'))