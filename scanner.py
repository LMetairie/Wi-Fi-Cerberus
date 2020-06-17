import pyshark
import threading
import json
import requests
from datetime import datetime
import time

class Probe:
    def __init__(self, datetime, mac, signal_strenght, distance):
        self.datetime = datetime
        self.mac = mac
        self.signal_strenght = signal_strenght
        self.distance = distance


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
    cap = pyshark.LiveCapture(interface='wlan0mon',display_filter='wlan.fc.subtype==0x0004')

    while(True):
        start = time.time()
        end = 0
        list_of_probes =[]

        for packet in cap.sniff_continuously():

            puissance = -34
            rssi = int(packet.radiotap.dbm_antsignal)
            distance = pow(10, (puissance - rssi) / 20)

            probe = {
                "created_at" : "{}".format(datetime.now()),
                "field1" : packet.wlan.sa_resolved,
                "field2" : packet.radiotap.dbm_antsignal,
                "field3" : distance
                }

            list_of_probes.append(probe)
            end = time.time()
            #For the "for" loop.
            if end - start > 16:
                break
        
        send_json_to_TS(list_of_probes)

getLiveConnexion()




    
        
            

