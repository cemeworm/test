import random 
from urllib.request import urlretrieve
import os

url='http://www.moguproxy.com/proxy/validateCode/createCode?time={}'
path = os.path.dirname(__file__) + '/origin_imgs/'

for i in range(15318786040083,1531878604300):
    urlretrieve(url.format(i),path + str(i)[-3:] + '.jpg')
    print("success in downloading {} pieces of photo".format(str(i)[-3:]))