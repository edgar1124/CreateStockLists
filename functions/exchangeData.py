from time import sleep
import pandas as pd
from polygon import RESTClient

def GetData ():
    
  if __name__ == '__main__':
    import sys
    sys.path.append('/Users/ed/CodingOnMac/StockAnalysis/CreateStockLists/')
    from ignore import settings
    key = settings.key
  else:
    from ignore.settings import key

  client = RESTClient(api_key = key)

  exchange_data = pd.DataFrame(client.get_exchanges(asset_class='stocks', locale='us'))
  sleep(20)

  exchange_list = list(set(exchange_data.mic))
  #exchange_list = [e for e in exchange_list if e is not None]

  inactive_exchanges = ['OOTC', 'BATS', 'BATY', 'CBSX', 'EPRL', 'EDGA', 'EDGX', \
                        'FINC', 'FINN', 'FINY', 'IEXG', 'LTSE', 'MEMX', 'XADF', \
                          'XBOS', 'XCHI', 'XISE', 'XCIS', 'XPHL', None]

  # ARCX, XASE, XNAS, XNYS are active echanges
  # ARCX may be only ETFs

  for inactive in inactive_exchanges:
    try:
      exchange_list.remove(inactive)
    except Exception as e:
      pass    

  return(exchange_list, client)

if __name__ == '__main__':

  print(GetData())
