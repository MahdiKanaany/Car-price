import requests as re
import json
w = open('json.txt','a')
token = 'ef8c48f8416a982372028e7aef4d8357'
url = 'https://sourcearena.ir/api/?token=%s&car=all'%(token)
response = re.get(url).json()
w.write(str(response))
w.close()
for item in response:
    print(item['model'])