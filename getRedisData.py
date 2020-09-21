# import redis

# r = redis.Redis(
# host='hostname',
# port=port,
# password='password')

# from time import gmtime, strftime


import redis

hostnameMacan = '10.244.125.197'
port = 6379
password = '9ff7b9d0-891b-4980-8559-6a67a76a73ac'

rMacan = redis.Redis(
host=hostnameMacan,
# port=port,
)

from datetime import datetime
timeNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

print(timeNow)

# print(rjs3.hgetall('pms1'))
# print(rjs4.hgetall('pms10'))
# print(rjs5.hgetall('pms1'))
# rjs3.hget('pms'+str(x),'voltage')
print(rMacan.hget('pms1','voltage'))


# f = open("D:/Sundaya/File JS Pro/Joulstore rev 2 ehub only/demofile3.txt", "r")
# print(f.read())

# for x in range (1,17):

    # print(rjs3.hgetall('pms'+str(x)))
    # print(str(rjs3.hgetall('pms'+str(x))) + "\n")
    # # print(rjs5.hgetall('pms'+str(x)))
    # f3 = open("D:/Sundaya/File JS Pro/Joulstore rev 2 ehub only/datajs3/pack"+str(x)+".txt", "a")
    # f3.write(str(timeNow) +" " + str(rjs3.hgetall('pms'+str(x)))+"\n")
    # f3.close()

#     f4 = open("D:/Sundaya/File JS Pro/Joulstore rev 2 ehub only/datajs4/pack"+str(x)+".txt", "a")
#     f4.write(str(timeNow) +" " + str(rjs4.hgetall('pms'+str(x)))+"\n")
#     f4.close()

#     f5 = open("D:/Sundaya/File JS Pro/Joulstore rev 2 ehub only/datajs5/pack"+str(x)+".txt", "a")
#     f5.write(str(timeNow) +" " + str(rjs5.hgetall('pms'+str(x)))+"\n")
#     f5.close()






    # dataV =rjs5.hget('pms'+str(x),'voltage')
    # dataV = dataV.decode('utf-8')
    # print(dataV)
    # getV =float( rjs1.hget('pms'+str(x),'voltage').decode('utf-8'))/100
    # getA =float( rjs1.hget('pms'+str(x),'current').decode('utf-8'))/10
    # getD =rjs1.hget('pms'+str(x),'dmos_state').decode('utf-8')

    # getV = rjs3.hget('pms'+str(x),'voltage')
    # getA = rjs3.hget('pms'+str(x),'current')
    # getD = rjs3.hget('pms'+str(x),'dmos_state')
    # getV =float( rMacan.hget('pms'+str(x),'voltage').decode('utf-8'))/100
    # getA =float( rMacan.hget('pms'+str(x),'current').decode('utf-8'))/10
    # getD =rMacan.hget('pms'+str(x),'dmos_state').decode('utf-8')
    # print("pack " + str(x) +" "+ str(getV) + " " + str(getA)+ " " + str(getD))
