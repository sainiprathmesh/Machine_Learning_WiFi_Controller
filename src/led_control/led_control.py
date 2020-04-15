from boltiot import Bolt

api_key = "Your API Key"
device_id = "BOLT1488XXXX"
mybolt = Bolt(api_key, device_id)
print("_____MENU_____\n1.ON\n2.OFF")
s = input()
if s == "1":
    response = mybolt.digitalWrite('0', 'HIGH')
    print(response)
elif s == "2":
    response1 = mybolt.digitalWrite('0', 'LOW')
    print(response1)
