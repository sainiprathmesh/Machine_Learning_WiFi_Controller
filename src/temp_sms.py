import json
import time

from boltiot import Bolt, Sms

from src import conf

minimum_limit = 300
maximum_limit = 600
mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)
while True:
    print("Reading sensor value")
    response = mybolt.analogRead('A0')
    data = json.loads(response)
    sensor_value = int(data['value'])
    print("Sensor value is: " + str((100 * sensor_value) / 1024))
    try:
        if sensor_value > maximum_limit or sensor_value < minimum_limit:
            print("Making request to Twilio to send a SMS")
            response = sms.send_sms("The Current temperature sensor value is " + str((100 * sensor_value) / 1024))
            print("Response received from Twilio is: " + str(response))
            print("Status of SMS at Twilio is :" + str(response.status))
    except Exception as e:
        print("Error occured: Below are the details")
        print(e)
    time.sleep(10)
