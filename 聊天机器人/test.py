import requests
import json

apiUrl = 'http://www.tuling123.com/openapi/api'

data1 = {
    "key": '145313d8474543db91d4ba5ecf01b4cb',
    "info": 'hello',
    "userid": '123'
}

r = requests.post(apiUrl,data=data1).json()

print(r.get('text'))