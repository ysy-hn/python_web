import time
import requests


start = time.time()
requests.get('http://www.sohu.com')
print('cost: {}s'.format(time.time() - start))

