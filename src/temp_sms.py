from boltiot import Bolt, Sms

from src import conf

minimum_limit = 300
maximum_limit = 600
mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)
