from boltiot import Bolt

api_key = "a425c725-e879-4e29-a423-a9fd223e9e09"
device_id = "BOLT14883313"
mybolt = Bolt(api_key, device_id)
response = mybolt.isOnline()
