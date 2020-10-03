import atexit
import json
import os
import sys
import threading
import time
from datetime import datetime

import pyshark
import requests
from mac_vendor_lookup import MacLookup
from prettytable import PrettyTable


@atexit.register
def leaving():
    print("You are now leaving the Python sector.")


def print_probe(probe, table):
    print_probe.counter += 1

    os.system("clear")

    values = list(probe.values())
    table.field_names = ["No.", "Date", "MAC", "Puissance Signal", "Distance", "Vendor"]
    table.add_row(
        [print_probe.counter, values[0], values[1], values[2], values[3], values[4]]
    )

    if print_probe.counter > 25:
        table.del_row(0)

    print(table)


def send_json_to_TS(list_of_probes):
    header = {"Content-type": "application/json"}
    url = "https://api.thingspeak.com/channels/1062874/bulk_update.json"
    json_final = {"write_api_key": "ULRXXCBWF73UO8GZ", "updates": list_of_probes}
    obj = json.dumps(json_final)
    response = requests.request("POST", url, headers=header, data=obj)
    print(response)


def getLiveConnexion():
    print("Starting monitoring mode...")
    cap = pyshark.LiveCapture(
        interface="wlan0mon", display_filter="wlan.fc.subtype==0x0004"
    )
    print("Listening for beacon packets..")

    list_of_probes = []
    list_of_detected_devices = []

    ## Definition du pretty table
    table = PrettyTable()
    print_probe.counter = 0
    list_of_detected_devices.clear()

    while True:
        # list_of_detected_devices.clear()
        list_of_probes.clear()

        start = time.time()
        end = 0

        for packet in cap.sniff_continuously():

            ## Si ladresse mac a deja etait detctee une fois, on saut ce packet.
            if packet.wlan.sa_resolved in list_of_detected_devices:
                continue
            else:
                list_of_detected_devices.append(packet.wlan.sa_resolved)

            puissance = 5
            rssi = int(packet.radiotap.dbm_antsignal)
            distance = pow(10, (puissance - rssi) / 20)
            try:
                vendor = MacLookup().lookup(packet.wlan.sa_resolved)
            except Exception:
                vendor = "Unknown"

            probe = {
                "created_at": "{}".format(datetime.now()),
                "field1": packet.wlan.sa_resolved,
                "field2": packet.radiotap.dbm_antsignal,
                "field3": distance,
                "field4": vendor,
            }

            time.sleep(2)
            print_probe(probe, table)

            list_of_probes.append(probe)
            end = time.time()

            if end - start > 5:
                break
        # print(list_of_probes)
        # send_json_to_TS(list_of_probes)


# Define main later.
getLiveConnexion()
