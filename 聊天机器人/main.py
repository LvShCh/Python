#coding = utf-8

import requests
import itchat

KEY = '145313d8474543db91d4ba5ecf01b4cb'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key' : KEY,
        'info' : msg,
        'userid' : '123456',
    }
    try:
        r = requests.post(apiUrl,data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)

def tuling_reply(msg):
    defaultReply = 'zs is really sb'
    reply = get_response(msg['Text'])
    return reply or defaultReply

itchat.auto_login(hotReload=True)
itchat.run()