from boltiot import Bolt

from src.temp_alert import conf

mybolt = Bolt(conf.bolt_api_key, conf.device_id)
