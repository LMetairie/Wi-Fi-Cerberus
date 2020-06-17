import json
import time

class Probe:
    def __init__(self, datetime, mac, signal_strenght, distance):
      self.datetime = datetime
      self.mac = mac
      self.signal_strenght = signal_strenght
      self.distance = distance

x = Probe(time.CLOCK_REALTIME,'10:25:01:25:12','-34','2.0')

print(json.dumps(x))