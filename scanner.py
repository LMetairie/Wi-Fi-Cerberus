import pyshark

def getLiveConnexion(timeout1):
    cap = pyshark.LiveCapture(interface='wlan0mon',display_filter='wlan.fc.subtype==0x0004')

    list_user =[]

    for packet in cap.sniff_continuously():
        puissance = -34
        rssi = int(packet.radiotap.dbm_antsignal)
        distance = pow(10, (puissance - rssi) / 20)
        
        if(packet.wlan.sa_resolved not in list_user):
            print('Mac Source: ', packet.wlan.sa_resolved, 'Force du signal : {} dBm'.format(packet.radiotap.dbm_antsignal),' Distance : {:.2f} m'.format(distance))
            list_user.append(packet.wlan.sa_resolved)

getLiveConnexion(20)
