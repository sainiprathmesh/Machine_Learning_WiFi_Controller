from boltiot import Bolt

api_key = "a425c725-e879-4e29-a423-a9fd223e9e09"
device_id = "BOLT14883313"
mybolt = Bolt(api_key, device_id)
print("_____MENU_____\n1.ON\n2.OFF")
s = input()
if s == "1":
    response = mybolt.digitalWrite('0', 'HIGH')
    print(response)
elif s == "2":
    response1 = mybolt.digitalWrite('0', 'LOW')
    print(response1)
