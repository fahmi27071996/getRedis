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
print("pulau macan")
for x in range(1,25):
    getV = r.hget('pms'+str(x),'voltage')
    getA = r.hget('pms'+str(x),'current')
    getD = r.hget('pms'+str(x),'dmos_state')
    getC = r.hget('pms'+str(x),'cmos_state')
    print("pack " + str(x) +" "+ str(getV) + " " + str(getA)+ " " + str(getD)+ " " + str(getC))