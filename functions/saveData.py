import csv, pickle

def WriteToCSV (ticker_file_name, tickers_for_csv):

  with open(ticker_file_name, mode='w') as fp:
    stock_writer = csv.writer(fp, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    stock_writer.writerow(tickers_for_csv)

  return

def WriteToPickle (ticker_file_name, tickers_for_pickle):

  with open(ticker_file_name, 'wb') as fp:
    pickle.dump(tickers_for_pickle, fp)

  return



if __name__ == '__main__':
  
  test_data = ["Hello", "My", "Name", "is", "John"]
    
  #WriteToCSV(test_data)
  WriteToPickle('test_data', test_data)