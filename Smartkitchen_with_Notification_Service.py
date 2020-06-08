import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
import requests
#Provide your IBM Watson Device Credentials
organization = "9u9gxc"
deviceType = "Raspberrypi"
deviceId = "123456"
authMethod = "token"
authToken = "12345678"

def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)#Commands
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()
	
# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()
while True:
        
        jar1=random.randint(0, 100)
        if jar1 < 10:
                print("Kaju needs to refill")
                url = "https://www.fast2sms.com/dev/bulk"
                querystring = {"authorization":"I4yrX8QM5S7TPCxRsEufdemLFq6nw0ObptBGoNDvaH1WhKUcj3PqhLwzya62flxE8XpRBeOsm3CVKTiY","sender_id":"FSTSMS","message":"Kaju needs to refill","language":"english","route":"p","numbers":"7013831615"}
                headers = {
                        'cache-control': "no-cache"
                        }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)
        elif jar1 < 50:
                print("Kaju at 50%")
        elif jar1 <80:
                print("Kaju is almost full")
        else:
                print("Kaju is full")
        jar2=random.randint(0, 100)
        if jar2 < 10:
                print("Badam needs to refill")
                url = "https://www.fast2sms.com/dev/bulk"
                querystring = {"authorization":"I4yrX8QM5S7TPCxRsEufdemLFq6nw0ObptBGoNDvaH1WhKUcj3PqhLwzya62flxE8XpRBeOsm3CVKTiY","sender_id":"FSTSMS","message":"Badam needs to refill","language":"english","route":"p","numbers":"7013831615"}
                headers = {
                        'cache-control': "no-cache"
                        }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)
        elif jar2 < 50:
                print("Badam at 50%")
        elif jar2 <80:
                print("Badam is almost full")
        else:
                print("Badam is full")
        jar3=random.randint(0, 100)
        if jar3 < 10:
                print("Pista needs to refill")
                url = "https://www.fast2sms.com/dev/bulk"
                querystring = {"authorization":"I4yrX8QM5S7TPCxRsEufdemLFq6nw0ObptBGoNDvaH1WhKUcj3PqhLwzya62flxE8XpRBeOsm3CVKTiY","sender_id":"FSTSMS","message":"Pista needs to refill","language":"english","route":"p","numbers":"7013831615"}
                headers = {
                        'cache-control': "no-cache"
                        }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)
        elif jar3 < 50:
                print("Pista at 50%")
        elif jar3 <80:
                print("Pista is almost full")
        else:
                print("Pista is full")
        
        lpg=random.randint(10, 20)
        if lpg < 15:
                print("lpg at 50%")
        elif lpg < 12:
                print("lpg at low")
        elif lpg >=10:
                print("LPG needs to refill")
                url = "https://www.fast2sms.com/dev/bulk"
                querystring = {"authorization":"I4yrX8QM5S7TPCxRsEufdemLFq6nw0ObptBGoNDvaH1WhKUcj3PqhLwzya62flxE8XpRBeOsm3CVKTiY","sender_id":"FSTSMS","message":"LPG needs to refill","language":"english","route":"p","numbers":"7013831615"}
                headers = {
                        'cache-control': "no-cache"
                        }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)
        else:
                print("lpg is full")
        gas_leak=random.randint(0,10)
        if  gas_leak > 0:
                print("Gas leakage detected at LPG")
                url = "https://www.fast2sms.com/dev/bulk"
                querystring = {"authorization":"I4yrX8QM5S7TPCxRsEufdemLFq6nw0ObptBGoNDvaH1WhKUcj3PqhLwzya62flxE8XpRBeOsm3CVKTiY","sender_id":"FSTSMS","message":"Gas leakage detected at LPG","language":"english","route":"p","numbers":"7013831615"}
                headers = {
                        'cache-control': "no-cache"
                        }
                response = requests.request("GET", url, headers=headers, params=querystring)
                print(response.text)
        else:
                print("No gas leakage detected")
        
        #Send jar1 & jar2 & jar3 & lpg & gas_leakage_sensor to IBM Watson
        data = { 'Kaju' : jar1, 'Badam': jar2, 'Pista': jar3, 'lpg': lpg, 'gas_leakage_detector': gas_leak, }
        #print (data)
        def myOnPublishCallback():
            print ("Published Kaju = %sQ" % jar1, "Badam = %sQ" % jar2, "Pista = %sQ" % jar3, "lpg = %sKg" % lpg, "gas_leakage_detector = %s " % gas_leak, "to IBM Watson")
        success = deviceCli.publishEvent("smartkitchen", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(2)
        deviceCli.commandCallback = myCommandCallback        
# Disconnect the device and application from the cloud
deviceCli.disconnect()
