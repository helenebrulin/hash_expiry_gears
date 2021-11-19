from gearsclient import GearsRemoteBuilder as GB
from gearsclient import execute
import redis

client = redis.Redis(host='localhost', port=6379)


client.hset("test1", "field", "value")
client.hset("test2", "field", "value")
client.hset("test3", "field", "value")
client.sadd("set", "test1", "test2", "test3")
client.expire("test1", 15)


cap = GB('KeysReader')
cap.foreach(lambda x:
    execute('SREM', 'set', x['key']))
cap.register(prefix='*',
    keyTypes=['hash'],
    mode='sync',
    eventTypes=['expired'],
    readValue=True)



# CLI
# RG.PYEXECUTE "GB('KeysReader').foreach(lambda x: execute('SREM', 'set', x['key'])).register(prefix='*',mode='sync',eventTypes=['expired'],keyTypes=['hash'],readValue=False)"
