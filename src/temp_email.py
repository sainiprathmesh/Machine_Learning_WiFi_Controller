from boltiot import Bolt

from src import email_conf

minimum_limit = 300
maximum_limit = 600
mybolt = Bolt(email_conf.API_KEY, email_conf.DEVICE_ID)
