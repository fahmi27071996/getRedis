# import redis

# r = redis.Redis(
# host='hostname',
# port=port,
# password='password')


import redis

hostname = 'localhost'
port = 6379
#password = '9ff7b9d0-891b-4980-8559-6a67a76a73ac'
r = redis.Redis(
host=hostname,
port=port,
#password=password
)

getData = r.hget('pms6','voltage')

print(getData)