import pyshark
import threading
import json
import requests
from datetime import datetime
import time
from mac_vendor_lookup import MacLookup


# class Probe:
#     def __init__(self, datetime, mac, signal_strenght, distance, vendor):
#         self.datetime = datetime
#         self.mac = mac
#         self.signal_strenght = signal_strenght
#         self.distance = distance
#         self.vendor = vendor


def send_json_to_TS(list_of_probes):
    header = {"Content-type": "application/json"}
    url = "https://api.thingspeak.com/channels/1062874/bulk_update.json"
    json_final = {
        "write_api_key":"ULRXXCBWF73UO8GZ",
        "updates":list_of_probes    
    }
    obj = json.dumps(json_final)
    response = requests.request("POST", url, headers=header, data = obj)
    print(response)


def getLiveConnexion():
    print("Starting monitoring mode...")
    cap = pyshark.LiveCapture(interface='wlan0mon',display_filter='wlan.fc.subtype==0x0004')
    print("Listening for beacon packets..")

    list_of_probes =[]
    list_of_detected_devices = []

    while(True):
        list_of_detected_devices.clear()
        list_of_probes.clear()

        start = time.time()
        end = 0

        for packet in cap.sniff_continuously():
            # Si l'adresse mac a deja etait detctée une fois, on saut ce packet.
            if packet.wlan.sa_resolved in list_of_detected_devices:
                continue
            else:
                list_of_detected_devices.append(packet.wlan.sa_resolved)

            puissance = -34
            rssi = int(packet.radiotap.dbm_antsignal)
            distance = pow(10, (puissance - rssi) / 20)
            vendor=MacLookup().lookup(packet.wlan.sa_resolved)

            probe = {
                "created_at" : "{}".format(datetime.now()),
                "field1" : packet.wlan.sa_resolved,
                "field2" : packet.radiotap.dbm_antsignal,
                "field3" : distance,
                "field4" : vendor
                }

            list_of_probes.append(probe)
            end = time.time()
            #For the "for" loop.
            if end - start > 16:
                break 
        print(list_of_probes) 
        # send_json_to_TS(list_of_probes)

getLiveConnexion()




    
        
            

