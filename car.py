import requests as re
token = 'ef8c48f8416a982372028e7aef4d8357'
url = 'https://sourcearena.ir/api/?token=%s&car=all'%(token)
print(re.get(url).json())
